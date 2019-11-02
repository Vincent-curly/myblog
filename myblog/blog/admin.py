from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.contrib.admin.models import LogEntry

from .models import Post, Category, Tag
from .adminforms import PostAdminForm
from myblog.custom_site import custom_site
from myblog.base_admin import BaseOwnerAdmin


class PostInline(admin.TabularInline):  # 可以选择继承自 admin.StackedInline,以获取不同的展示样式
    fields = ('title', 'desc')
    extra = 1   # 控制额外多几个
    model = Post

# Register your models here.
@admin.register(Category, site=custom_site)
class CategoryAdmin(BaseOwnerAdmin):
    inlines = [PostInline, ]
    list_display = ('name', 'status', 'is_nav', 'created_time', 'post_count')
    fields = ('name', 'status', 'is_nav')

    def post_count(self, obj):
        return obj.post_set.count()

    post_count.short_description = '文章数量'


@admin.register(Tag, site=custom_site)
class TagAdmin(BaseOwnerAdmin):
    list_display = ('name', 'status', 'created_time')
    fields = ('name', 'status')


class CategoryOwnerFilter(admin.SimpleListFilter):
    """ 自定义过滤器，只显示当前用户分类 """
    title = '分类过滤器'
    parameter_name = 'owner_category'

    def lookups(self, request, model_admin):
        return Category.objects.filter(owner=request.user).values_list('id', 'name')

    def queryset(self, request, queryset):
        category_id = self.value()
        if category_id:
            return queryset.filter(category_id=self.value())
        return queryset


@admin.register(Post, site=custom_site)
class PostAdmin(BaseOwnerAdmin):
    form = PostAdminForm
    list_display = [
        'title', 'category', 'status',
        'owner', 'created_time', 'operator'
    ]
    list_display_links = []

    # list_filter = ['category', ]
    list_filter = [CategoryOwnerFilter, ]
    search_fields = ['title', 'category__name']
    save_on_top = True

    actions_on_top = True
    actions_on_bottom = True

    # 编辑页面
    save_on_top = True
    exclude = ['owner']
    """
    fields = (
        ('category', 'title'),
        'desc',
        'status',
        'content',
        'tag',
    )
    """
    fieldsets = (
        ('基础配置', {
            'description': '基础配置描述',
            'fields': (
                ('title', 'category'),      # 显示多个字段在同一行, 包裹这些字段在一个元组,title 和 category 将同行显示
                'status',
            ),
        }),
        ('内容', {
            'fields': (
                'desc',
                'content',
            ),
        }),
        ('额外信息', {
            # 'classes': ('collapse',),
            'classes': ('wide',),
            'fields': ('tag', ),
        })
    )
    filter_horizontal = ('tag', )   # 选和不选选项框水平方向上并排出现
    # filter_vertical = ('tag', )   # 垂直界面，不选选项框在选选项框上面

    def operator(self, obj):
        return format_html(
            '<a href="{}">编辑</a>',
            # reverse('admin:blog_post_change', args=(obj.id,))
            reverse('cus_admin:blog_post_change', args=(obj.id,))
        )
    operator.short_description = '操作'

    class Media:
       css = {
           'all': ("http://cdn.bootcss.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css", ),
       }
       js = ('http://cdn.bootcss.com/bootstrap/4.0.0-beta.2/js.bootstrap.bundle.js', )


@admin.register(LogEntry, site=custom_site)
class LogEntryAdmin(admin.ModelAdmin):
    list_display = ['object_repr', 'object_id', 'action_flag', 'user', 'change_message']