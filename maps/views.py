from django.shortcuts import render

# Create your views here.
import folium   # 지도 사용
def home(request):
    mf = folium.Map([37.532920, 126.892814], zoom_start=10)
    mf = mf._repr_html_()
    first = 'Dong K'
    result = {'mapfolium':mf, 'f01':first}
    return render(request, template_name='maps/home.html',context=result)

def plotly(request):
    xValues = [50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150];
    yValues = [7, 8, 8, 9, 9, 9, 10, 11, 14, 14, 15];
    result = {'x_val':xValues, 'y_val':yValues}
    # result {dict}형으로 html에 던져준다.
    xValues1 = [50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150];
    yValues1 = [7, 8, 8, 9, 9, 9, 10, 11, 14, 14, 15];
    result['x_val1'] = xValues1
    result['y_val1'] = yValues1
    return render(request, template_name='maps/plotly.html', context=result)