from django.shortcuts import render

# Create your views here.
import sqlite3
def list(request):
    result = dict()
    connect = sqlite3.connect('db.sqlite3')
    connect.row_factory = sqlite3.Row   # for getting columns
    cursor = connect.cursor()
    # economics
    cursor.execute('select * from polls_economics pe')
    data = cursor.fetchall()    # cursor에서 값들을 모두 추출
    for row in data :
        print(row['title'], ' : ', row['href'])
    result['erows'] = data

    # user
    cursor.execute('select * from auth_user au')
    result['members'] = cursor.fetchall()
    for row in result['members']:
        print(row['username'], ', ', row['email'])

    return render(request, 'board/list.html', result)

from django.core.paginator import Paginator
def list_paginator(request):
    connect = sqlite3.connect('db.sqlite3')
    connect.row_factory = sqlite3.Row  # for getting columns
    cursor = connect.cursor()
    # economics
    cursor.execute('select * from polls_economics pe')
    data = cursor.fetchall()
    for row in data:
        print(row['title'], row['href'])
    paginator = Paginator(data, 5)
    result = dict()
    result['paginator'] = paginator
    # request.GET['page'] # 그냥하면 error, function이 필요
    page_number = request.GET.get('page', 1)
    result['page_obj'] = paginator.get_page(page_number)
    return render(request, 'board/list_paginator.html', context=result)