from django.contrib.auth.decorators import login_required
from thing.stuff import render_page

@login_required()
def trade_tool(request):
    out = render_page(
        'thing/trade_tool.html',    # template
        {},                         # data
        request                     # request
    )
    return out