from django.shortcuts import render

# Create your views here.
import folium   # 지도 사용
def home(request):
    mf = folium.Map([37.532920, 126.892814], zoom_start=10)
    mf = mf._repr_html_()
    first = 'Dong K'
    result = {'mapfolium':mf, 'f01':first}
    return render(request, template_name='maps/home.html',context=result)
