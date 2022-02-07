# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from spotify_auth.models import Artist
from .models import Vote

def index(request):
    print("inside index")
    artists = Artist.objects.filter().iterator()
    artist_names = []
    artist_images = []
    votes = Vote.objects.get(pk=44)
    votes2 = Vote.objects.get(pk=45)
    votes3 = Vote.objects.get(pk=46)
    votes4 = Vote.objects.get(pk=47)

    for item in artists:
        artist_names.append(item.artist)
        artist_images.append(item.a_img)
    context = {
        'artists': artist_names,
        'images': artist_images,
        'votes': votes,
        'votes2': votes2,
        'votes3': votes3,
        'votes4': votes4,
    }
    return render(request, 'tournament/tournament.html', context=context)


def vote_bracket(request):

    print("inside vote_bracket")
    artists = Artist.objects.filter().iterator()
    artist_names = []
    for item in artists:
        artist_names.append(item.artist)

    print(artist_names)
    vote = Vote.objects.get(pk=40)

    vote2 = Vote.objects.get(pk=41)

    vote3 = Vote.objects.get(pk=42)

    vote4 = Vote.objects.get(pk=43)

    '''selected_option = request.POST['clear']
    if selected_option == 'option':
        print("clearing")
        vote.option_0_count = 0
        vote.option_1_count = 0
        vote.option_2_count = 0
        vote.option_3_count = 0
        vote.option_4_count = 0
        vote.option_5_count = 0
        vote.option_6_count = 0
        vote.option_7_count = 0
        vote.option_8_count = 0
        vote.option_9_count = 0
        vote.option_10_count = 0
        vote.option_11_count = 0
        vote.option_12_count = 0
        vote.option_13_count = 0
        vote.option_14_count = 0
        vote.option_15_count = 0
        vote2.option_0_count = 0
        vote2.option_1_count = 0
        vote2.option_2_count = 0
        vote2.option_3_count = 0
        vote2.option_4_count = 0
        vote2.option_5_count = 0
        vote2.option_6_count = 0
        vote2.option_7_count = 0
        vote3.option_0_count = 0
        vote3.option_1_count = 0
        vote3.option_2_count = 0
        vote3.option_3_count = 0
        return HttpResponseRedirect(reverse('tournament'))'''

    if request.method == 'POST':
        print("Starting round 1")
        if request.method == 'POST':
            vote.option_0_count = 0
            vote.option_1_count = 0
            vote.option_2_count = 0
            vote.option_3_count = 0
            vote.option_4_count = 0
            vote.option_5_count = 0
            vote.option_6_count = 0
            vote.option_7_count = 0
            vote.option_8_count = 0
            vote.option_9_count = 0
            vote.option_10_count = 0
            vote.option_11_count = 0
            vote.option_12_count = 0
            vote.option_13_count = 0
            vote.option_14_count = 0
            vote.option_15_count = 0
            vote2.option_0_count = 0
            vote2.option_1_count = 0
            vote2.option_2_count = 0
            vote2.option_3_count = 0
            vote2.option_4_count = 0
            vote2.option_5_count = 0
            vote2.option_6_count = 0
            vote2.option_7_count = 0
            vote3.option_0_count = 0
            vote3.option_1_count = 0
            vote3.option_2_count = 0
            vote3.option_3_count = 0

            selected_option = request.POST['pair0']
            if selected_option == 'option0':
                vote.option_0_count += 1
                vote.winner1 = artist_names[0]
            elif selected_option == 'option1':
                vote.option_1_count += 1
                vote.winner1 = artist_names[1]
            else:
                return HttpResponse(400, 'Invalid form')
            print(vote.winner1)

            selected_option = request.POST['pair1']
            if selected_option == 'option2':
                vote.option_2_count += 1
                vote.winner2 = artist_names[2]
            elif selected_option == 'option3':
                vote.option_3_count += 1
                vote.winner2 = artist_names[3]
            else:
                return HttpResponse(400, 'Invalid form')
            print(vote.winner2)

            selected_option = request.POST['pair2']
            if selected_option == 'option4':
                vote.option_4_count += 1
                vote.winner3 = artist_names[4]
            elif selected_option == 'option5':
                vote.option_5_count += 1
                vote.winner3 = artist_names[5]
            else:
                return HttpResponse(400, 'Invalid form')
            print(vote.winner3)

            selected_option = request.POST['pair3']
            if selected_option == 'option6':
                vote.option_6_count += 1
                vote.winner4 = artist_names[6]
            elif selected_option == 'option7':
                vote.option_7_count += 1
                vote.winner4 = artist_names[7]
            else:
                return HttpResponse(400, 'Invalid form')
            print(vote.winner4)

            selected_option = request.POST['pair4']
            if selected_option == 'option8':
                vote.option_8_count += 1
                vote.winner5 = artist_names[8]
            elif selected_option == 'option9':
                vote.option_9_count += 1
                vote.winner5 = artist_names[9]
            else:
                return HttpResponse(400, 'Invalid form')
            print(vote.winner5)

            selected_option = request.POST['pair5']
            if selected_option == 'option10':
                vote.option_10_count += 1
                vote.winner6 = artist_names[10]
            elif selected_option == 'option11':
                vote.option_11_count += 1
                vote.winner6 = artist_names[11]
            else:
                return HttpResponse(400, 'Invalid form')
            print(vote.winner6)

            selected_option = request.POST['pair6']
            if selected_option == 'option12':
                vote.option_12_count += 1
                vote.winner7 = artist_names[12]
            elif selected_option == 'option13':
                vote.option_13_count += 1
                vote.winner7 = artist_names[13]
            else:
                return HttpResponse(400, 'Invalid form')
            print(vote.winner7)

            selected_option = request.POST['pair7']
            if selected_option == 'option14':
                vote.option_14_count += 1
                vote.winner8 = artist_names[14]
            elif selected_option == 'option15':
                vote.option_15_count += 1
                vote.winner8 = artist_names[5]
            else:
                return HttpResponse(400, 'Invalid form')
            print(vote.winner8)

            vote.round_started = 0
            '''+= 1'''
            vote.save()


    print("Starting round 2")
    if request.method == 'POST':
        vote2.option_0_count = 0
        vote2.option_1_count = 0
        vote2.option_2_count = 0
        vote2.option_3_count = 0
        vote2.option_4_count = 0
        vote2.option_5_count = 0
        vote2.option_6_count = 0
        vote2.option_7_count = 0

        selected_option = request.POST['pair0-2']
        if selected_option == 'option0':
            vote2.option_0_count += 1
            vote2.winner1 = vote.winner1
        elif selected_option == 'option1':
            vote2.option_1_count += 1
            vote2.winner1 = vote.winner2
        else:
            return HttpResponse(400, 'Invalid form')
        print(vote2.winner1)

        selected_option = request.POST['pair1-2']
        if selected_option == 'option2':
            vote2.option_2_count += 1
            vote2.winner2 = vote.winner3
        elif selected_option == 'option3':
            vote2.option_3_count += 1
            vote2.winner2 = vote.winner4
        else:
            return HttpResponse(400, 'Invalid form')
        print(vote2.winner2)

        selected_option = request.POST['pair2-2']
        if selected_option == 'option4':
            vote2.option_4_count += 1
            vote2.winner3 = vote.winner4
        elif selected_option == 'option5':
            vote2.option_5_count += 1
            vote2.winner3 = vote.winner5
        else:
            return HttpResponse(400, 'Invalid form')
        print(vote2.winner3)
        selected_option = request.POST['pair3-2']
        if selected_option == 'option6':
            vote2.option_6_count += 1
            vote2.winner4 = vote.winner6
        elif selected_option == 'option7':
            vote2.option_7_count += 1
            vote2.winner4 = vote.winner7
        else:
            return HttpResponse(400, 'Invalid form')
        print(vote2.winner4)

        vote2.round_started = 0
            
        vote2.save()

        print("Starting round 3")
        vote3.option_0_count = 0
        vote3.option_1_count = 0
        vote3.option_2_count = 0
        vote3.option_3_count = 0

        selected_option = request.POST['pair0-3']
        if selected_option == 'option1':
            vote3.option_0_count += 1
            vote3.winner1 = vote2.winner1
        elif selected_option == 'option2':
            vote3.option_1_count += 1
            vote3.winner1 = vote2.winner2
        else:
            return HttpResponse(400, 'Invalid form')
        print(vote3.winner1)
        selected_option = request.POST['pair1-3']
        if selected_option == 'option3':
            vote3.option_0_count += 1
            vote3.winner2 = vote2.winner3
        elif selected_option == 'option4':
            vote3.option_1_count += 1
            vote3.winner2 = vote2.winner4
        else:
            return HttpResponse(400, 'Invalid form')
        print(vote3.winner2)

        print("Starting round 4")
        vote3.option_0_count = 0
        vote3.option_1_count = 0
        vote3.option_2_count = 0
        vote3.option_3_count = 0

        selected_option = request.POST['pair0-4']
        if selected_option == 'option1':
            vote4.option_0_count += 1
            vote4.winner1 = vote3.winner1
        elif selected_option == 'option2':
            vote4.option_1_count += 1
            vote4.winner1 = vote3.winner2
        else:
            return HttpResponse(400, 'Invalid form')
        print(vote4.winner1)

        return HttpResponseRedirect(reverse('tournament'))

    context = {
        'vote': vote,
        'vote2': vote2,
        'vote3': vote3,
        'vote4': vote4,
    }

    return render(request, 'tournament/tournament.html', context=context)

'''def delete_data(request):
    all_votes = Vote.objects.filter().iterator()
    all_artists = Artist.objects.filter().iterator()
    for item in all_votes:
        item.delete()

    for item in all_artists:
        item.delete()'''
