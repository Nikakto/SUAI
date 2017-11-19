from django import template

from SUAI.staff.forms import NewsForm
from SUAI.models import News


register = template.Library()


@register.inclusion_tag('news.html', takes_context=True)
def news_block(context):

    news = News.objects.filter(removed=False).order_by('-date')
    news = news[:5]

    form = NewsForm()

    form.fields['title'].required = False
    form.fields['title'].widget.attrs['placeholder'] = 'News title'
    form.fields['title'].label = ""

    form.fields['content'].required = False
    form.fields['content'].widget.attrs['placeholder'] = 'News content'
    form.fields['content'].label = ""

    return {
        'context': context,
        'form': form,
        'news': news,
    }