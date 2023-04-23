from django.shortcuts import render, redirect, get_object_or_404
from django.core.handlers.wsgi import WSGIRequest

from django.http import Http404

from django.contrib.auth import login, logout, hashers, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings




from moderator.models import User,Moderator
from .decorator import moderator_only

from articles.models import (
    Article,
    ArticleColumn,
    Journal,
    Petition,
    Post,
)

from .forms import PostForm, JournalForm, ArticleColumnForm, BasicArticelForm, CKEditorForm, ModeratorUserForm, ArticleFullForm





# Dashboard
@login_required(login_url='login')
@moderator_only
def dashboard(request: WSGIRequest):
    data_not_viewed = Petition.objects.filter(is_viewed=False)

    data_sum_list = [
        len(Moderator.objects.all()),
        len(Article.objects.all()),
        len(Post.objects.all()),
        len(Journal.objects.all()),
        len(ArticleColumn.objects.all()),
        len(Petition.objects.all()),
    ]
    return render(request, 'moderator/index.html', {
        'data': data_not_viewed,
        'sums': data_sum_list,
    })




# Akkount viewslar
# ============================================================
# Profile View
@login_required(login_url='login')
@moderator_only
def profile_view(request: WSGIRequest):
    object = get_object_or_404(Moderator, user_id=request.user.id)
    data_filter = Petition.objects.filter(confirmed_id=object.pk)
    data_len = len(data_filter)
    return render(request, 'moderator/profile_view.html', {
        'object': object,
        'len_data': data_len,
        'data_filter': data_filter,
    })

# Profile update
@login_required(login_url='login')
@moderator_only
def profile_update(request: WSGIRequest):
    if request.method == 'POST':
        if request.POST.get('data_name') == 'other':
            first_name = request.POST.get('first_name', None)
            last_name = request.POST.get('last_name', None)
            email = request.POST.get('email', None)
            username = request.POST.get('username', None)
            dark_mode = request.POST.get('dark_mode', None)
            dark_mode = [True if dark_mode == 'on' else False][0]   

            if not (first_name and last_name and email and username):
                messages.error(request, message='Barcha bandlarni to\'ldiring !', extra_tags='danger')
                return redirect('profile_update')
            
            image = request.FILES.get('image', None)
            user = User.objects.get(pk=request.user.pk)
            user.first_name = first_name
            user.last_name = last_name
            user.username = username
            user.email = email
            user.dark_mode = dark_mode
            if image is not None:
                user.image = image
            user.save()
            login(request=request, user=user)
            messages.success(request, "Sozlamalar saqlandi!")
            return redirect('profile_view')
        
        elif request.POST.get('data_name') == 'password':
            old_password = request.POST.get('old_password', None)
            new_password = request.POST.get('new_password', None)
            new_password_again = request.POST.get('new_password_again', None)

            if not (old_password and new_password and new_password_again) or not (new_password == new_password_again):
                messages.error(request, "Parolni tadiqlashda xatolikka yo'l qo'ydingiz !", extra_tags='danger')
                return redirect('profile_update')
            
            user = User.objects.get(pk=request.user.pk)
            if not hashers.check_password(old_password ,user.password):
                messages.error(request, "Avvalgi parolni xato kiritdingiz !", extra_tags='danger')
                return redirect('profile_update')
            
            user.password = hashers.make_password(new_password)
            user.save()
            login(user=user, request=request)
            messages.success(request, "Parol muvaffaqiyatli o'zgartirildi !")
            return redirect('profile_view')
    return render(request, 'moderator/profile_update.html', {})




# Maqolalar viewslari
# ====================================================
# Barcha maqolalar
@login_required(login_url='login')
@moderator_only
def all_articles(request: WSGIRequest):
    data = Article.objects.all()
    return render(request, 'moderator/all_articles.html', {
        'data': data,
    })


@login_required(login_url='login')
@moderator_only
def article_read(request: WSGIRequest, pk):

    object = get_object_or_404(Article, pk=pk)

    return render(request, 'moderator/article_read.html', {
        'object': object,
    })


@login_required(login_url='login')
@moderator_only
def article_archive(request: WSGIRequest, pk):
    object = get_object_or_404(Article, pk=pk)
    object.is_active = [False if object.is_active == True else True][0]
    object.save()
    return redirect('article_read', pk=object.pk)



@login_required(login_url='login')
@moderator_only
def article_delete(request: WSGIRequest, pk):
    object = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        object.delete()
    return redirect('all_article')


@login_required(login_url='login')
@moderator_only
def article_change(request: WSGIRequest, pk):
    object = get_object_or_404(Article, pk=pk)
    form = ArticleFullForm(instance=object)

    if request.method == 'POST':
        form = ArticleFullForm(request.POST, instance=object)
        if form.is_valid:
            form.save()
            return redirect('article_read', pk=object.pk)

    return render(request, 'moderator/article_change.html', {
        'object': object,
        'form': form,
    })




# Maqolalar tugadi
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$4





# Postlar uchun viewslar 
# =====================================
# Barcha postlar
@login_required(login_url='login')
@moderator_only
def all_posts(request: WSGIRequest):
    data = Post.objects.all()
    return render(request, 'moderator/all_posts.html', {
        'data': data,
    })

# Yangi post qo'shish
@login_required(login_url='login')
@moderator_only
def post_create(request: WSGIRequest):
    try:
        moderator = Moderator.objects.get(user_id=request.user.id)
    except:
        return redirect('login')
    form = PostForm()
    if request.method == 'POST':
        data_form = PostForm(request.POST)
        
        if data_form.is_valid:
            object = data_form.save(commit=False)
            object.author = moderator
            object.save()
            messages.success(request, ''' Post saqlandi ''')
            return redirect('all_posts')
    return render(request, 'moderator/post_create.html', {
        'form': form,
    })

# Mavjud postni yangilash
@login_required(login_url='login')
@moderator_only
def post_update(request: WSGIRequest, pk):
    object = get_object_or_404(Post, pk=pk)
    form = PostForm(instance=object)

    if request.method == 'POST':
        data_form = PostForm(data=request.POST, instance=object)
        if data_form.is_valid:
            data_form.save(commit=True)
            messages.success(request, 'Sozlamalar saqlandi !')
            return redirect('all_posts')    
    return render(request, 'moderator/post_update.html', {
        'form': form,
        'object': object,
    })

# Potni o'chirish
@login_required(login_url='login')
@moderator_only
def post_delete(request: WSGIRequest, pk):
    object = get_object_or_404(Post, pk=pk)
    object.delete()
    messages.success(request, 'Post muvaffaqiyatli o\'chirildi')
    return redirect('all_posts')

# Postlar bo'limi tugadi
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$44




# Jurnallar viewslari
# =========================================
# Barcha jurnallar
@login_required(login_url='login')
@moderator_only
def journal_all(request: WSGIRequest):
    data = Journal.objects.all()
    return render(request, 'moderator/journal_all.html', {
        'data': data,
    })

# Yangi jurnal qo'shish
@login_required(login_url='login')
@moderator_only
def journal_create(request: WSGIRequest):
    form = JournalForm()
    if request.method == 'POST':
        form = JournalForm(request.POST)
        if form.is_valid:
            obj = form.save(commit=True)
            messages.success(request, 'Jurnal yaratildi. {obj.name}')
            return redirect('journal_all')
    return render(request, 'moderator/journal_create.html', {
        'form': form,
    })

# Mavjud jurnalni yangilash
@login_required(login_url='login')
@moderator_only
def journal_update(request: WSGIRequest, pk):
    object = get_object_or_404(Journal, pk=pk)
    form = JournalForm(instance=object)

    if request.method == 'POST':
        form = JournalForm(data=request.POST, instance=object)
        if form.is_valid:
            form.save()
            messages.success(request, 'Sozlamalar saqlandi')
            return redirect('journal_all')

    return render(request, 'moderator/journal_update.html', {
        'form': form,
        'object': object,
    })

# Jurnalni o'chirish
@login_required(login_url='login')
@moderator_only
def journal_delete(request: WSGIRequest, pk):
    object = get_object_or_404(Journal, pk=pk)
    messages.success('Jurnal o\'chirildi {object.name}')
    object.delete()
    return redirect('journal_all')

# Jurnallar bo'limi tugadi
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$4




# Maqola ruknlari
# ===============================================
# List view
@login_required(login_url='login')
@moderator_only
def article_col_all(request: WSGIRequest):
    data = ArticleColumn.objects.all()
    return render(request, 'moderator/article_col_all.html', {
        'data': data,
    })

# Rukn yaratish
@login_required(login_url='login')
@moderator_only
def article_col_create(request: WSGIRequest):
    form = ArticleColumnForm()

    if request.method == 'POST':
        form = ArticleColumnForm(data=request.POST)
        if form.is_valid:
            form.save()
            messages.success(request, 'Maqola rukni yaratildi.')
            return redirect('article_col_all')

    return render(request, 'moderator/article_col_create.html', {
        'form': form,
    })

# Ruknni yangilash
@login_required(login_url='login')
@moderator_only
def article_col_update(request: WSGIRequest, pk):
    object = get_object_or_404(ArticleColumn, pk=pk)
    form = ArticleColumnForm(instance=object)
    if request.method == 'POST':
        form = ArticleColumnForm(instance=object, data=request.POST)
        if form.is_valid:
            form.save()
            messages.success(request, 'Sozlamalar saqlandi.')
            return redirect('article_col_all')
    return render(request, 'moderator/article_col_update.html', {
        'object': object,   
        'form': form, 
    })


# Maqola ruknni o'chirish
@login_required(login_url='login')
@moderator_only
def article_col_delete(request: WSGIRequest, pk):
    if pk == 1:
        return redirect('article_col_all')
    object = get_object_or_404(ArticleColumn, pk=pk)
    object.delete()
    messages.success(request, 'Maqola rukni o\'chirildi.')
    return redirect('article_col_all')

# Ruknlar qismi tugadi
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$4




# Arizalar qismlari
# =========================================================
# Barcha arizalar
@login_required(login_url='login')
@moderator_only
def petition_all(request: WSGIRequest):
    data = Petition.objects.all().order_by('-pk')
    return render(request, 'moderator/petition_all.html', {
        'data': data,
    })



@login_required(login_url='login')
@moderator_only
def petition_detail(request: WSGIRequest, pk):
    object = get_object_or_404(Petition, pk=pk)
    
    return render(request, 'moderator/petition_detail.html', {
        'object': object,
    })


@login_required(login_url='login')
@moderator_only
def petition_access(request: WSGIRequest, pk):
    moderator = get_object_or_404(Moderator, user_id=request.user.id)
    object = get_object_or_404(Petition, pk=pk)

    form = BasicArticelForm()

    if request.method == 'POST':
        form = BasicArticelForm(request.POST)
        if form.is_valid:
            article = form.save(commit=False)
            article.confirmed = moderator
            article.title = object.title
            article.file = object.file
            article.description = object.description
            article.first_name = object.first_name
            article.last_name = object.last_name
            article.save()

            object.is_viewed = True
            object.status = Petition.STATUS[1][0]
            object.save()
            messages.success(request, ''' Ariza maqullandi va maqolalar safiga qo'shildi. ''')
            return redirect('all_article')
    return render(request, 'moderator/petition_accesss.html', {
        'object': object,
        'form': form,
    })


@login_required(login_url='login')
@moderator_only
def petition_not_access(request: WSGIRequest, pk):
    moderator = get_object_or_404(Moderator, user_id=request.user.id)
    object = get_object_or_404(Petition, pk=pk)
    object.is_viewed = True
    object.confirmed = moderator
    object.status = Petition.STATUS[3][0]
    object.save()

    messages.success(request, 'Ariza rad etildi.')

    # Email code here

    return redirect('petition_all')



@login_required(login_url='login')
@moderator_only
def petition_warning(request: WSGIRequest, pk):
    moderator = get_object_or_404(Moderator, user_id=request.user.id)
    object = get_object_or_404(Petition, pk=pk)
    form = CKEditorForm()

    if request.method == 'POST':
        form = CKEditorForm(request.POST)
        if form.is_valid:
            html_message = form['body'].value()
            # message mail here
            object.is_viewed = True
            object.confirmed = moderator
            object.status = Petition.STATUS[2][0]
            object.save()
            messages.success(request, 'Ariza qayta ko\'rib chiqish uchun rad etildi .')
            return redirect('petition_all')

    return render(request, 'moderator/petition_warning.html', {
        'form': form,
    })


# moderators 
# =========================================
# listview

@login_required(login_url='login')
@moderator_only
def moderator_all(request: WSGIRequest):
    data = Moderator.objects.all()
    moderator = get_object_or_404(Moderator, user_id=request.user.id)
    return render(request, 'moderator/moderator_all.html', {
        'data': data,
        'object': moderator
    })


@login_required(login_url='login')
@moderator_only
def moderator_detail(request: WSGIRequest, pk):
    object = get_object_or_404(Moderator, pk=pk)
    data_filter = Petition.objects.filter(confirmed_id=object.pk)
    len_data = len(data_filter)
    return render(request, 'moderator/moderator_detail.html', {
        'object': object,
        'data_filter': data_filter,
        'len_data': len_data,
    })

@login_required(login_url='login')
@moderator_only
def moderator_add(request: WSGIRequest):
    moderator = get_object_or_404(Moderator, user_id=request.user.pk)
    if moderator.is_created == False:
        raise Http404()
    form = ModeratorUserForm()

    if request.method == 'POST':
        form = ModeratorUserForm(request.POST)
        if form.is_valid:
            try:
                user = form.save(commit=False)
                user.dark_mode = False
                user.password = hashers.make_password(form['password'].value())
                user.save()
                new_moderator = Moderator()
                new_moderator.user = user
                new_moderator.role = request.POST.get('role', '')
                new_moderator.is_created = False
                new_moderator.save()
                messages.success(request, 'Yangi admin qo\'shildi. ')
                return redirect('moderator_all')
            except:
                messages.error(request, 'Iltimos boshqa username kiriting !', extra_tags='danger')

    return render(request, 'moderator/moderator_add.html', {
        'form': form,
    })



























































































def login_view(request: WSGIRequest):
    error_msg = None
    next_page = request.GET.get('next', None)
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        if username and password:
            user = authenticate(request=request, username=username, password=password)
            if user is not None:
                login(request=request, user=user)
                if next_page:
                    return redirect(next_page)
                return redirect('dashboard')
            else:
                error_msg = ''' Login yoki parol xato '''
        else:
            error_msg = ''' Barcha bandlar to'ldirilishi kerak ! '''

    return render(request, 'moderator/login.html', {
        'error_msg': error_msg,
    })


def logout_view(request):
    logout(request)
    return redirect('login')