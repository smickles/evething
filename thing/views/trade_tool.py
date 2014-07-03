from django.contrib.auth.decorators import login_required
import sys
from thing.stuff import render_page

@login_required()
def trade_tool(request):
    system = request.GET.get('system')
    if system:

        trade_plan = make_trade_plan(system)

        out = render_page(
            'thing/trade_tool.html',    # template
            {'trade_plan': trade_plan}, # data
            request                     # request
        )
        return out
    else:
        out = render_page(
            'thing/trade_tool.html',    # template
            {},                         # data
            request                     # request
        )
        return out

def make_trade_plan(system):
    if system == 'test':
        trade_plan = (
            ('Tritanium',                                               # Item
            'Jita 4-4 Caldari Business Tribunal Information Center',    # Pickup
            'Amarr 6-2 Theology Council Tribunal',                      # Drop off
            6.36,                                                       # Max Buy
            44000,                                                      # Amount
            7.63),                                                      # Min Sell
        )
        return trade_plan