from django.contrib.auth.decorators import login_required

@login_required()
def trade_tool(request):
    return