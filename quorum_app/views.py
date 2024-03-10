from django.shortcuts import render
from . import models
from django.db.models import Count, Case, When, IntegerField, Q
from .models import Legislator, Bill, Voteresult

def legislator_vote_stats(request):
    legislators = Legislator.objects.all()
    stats = []

    for legislator in legislators:
        supported_bills = Voteresult.objects.filter(legislator=legislator, vote_type=1).count()
        opposed_bills = Voteresult.objects.filter(legislator=legislator, vote_type=2).count()

        stats.append({
            'legislator': legislator,
            'supported_bills': supported_bills,
            'opposed_bills': opposed_bills,
        })

    return render(request, 'legislator_vote_stats.html', {'stats': stats})

def bill_vote_stats(request):
    legislators = Legislator.objects.annotate(
        supported_bills=Count(Case(When(voteresult__vote_type=1, then=1), output_field=IntegerField())),
        opposed_bills=Count(Case(When(voteresult__vote_type=2, then=1), output_field=IntegerField()))
    )

    bill_stats = []
    for bill in Bill.objects.all():
        supporters = Voteresult.objects.filter(vote__bill=bill, vote_type=1).count()
        opposers = Voteresult.objects.filter(vote__bill=bill, vote_type=2).count()


        primary_sponsor = bill.sponsor.name if (bill.sponsor_id and Legislator.objects.filter(id=bill.sponsor_id).exists()) else 'N/A'

        bill_stats.append({
            'bill_id': bill.id,
            'bill_title': bill.title,
            'supporters': supporters,
            'opposers': opposers,
            'primary_sponsor': primary_sponsor,
        })

    context = {'legislators': legislators, 'bill_stats': bill_stats}
    return render(request, 'bill_vote_stats.html', context)



def all_stats(request):
  
    legislators_stats = Legislator.objects.annotate(
        supported_bills=Count(Case(When(voteresult__vote_type=1, then=1), output_field=IntegerField())),
        opposed_bills=Count(Case(When(voteresult__vote_type=2, then=1), output_field=IntegerField()))
    )


    bill_stats = []
    for bill in Bill.objects.all():
        supporters = Voteresult.objects.filter(vote__bill=bill, vote_type=1).count()
        opposers = Voteresult.objects.filter(vote__bill=bill, vote_type=2).count()

        primary_sponsor = bill.sponsor.name if (bill.sponsor_id and Legislator.objects.filter(id=bill.sponsor_id).exists()) else 'N/A'

        bill_stats.append({
            'bill_id': bill.id,
            'bill_title': bill.title,
            'supporters': supporters,
            'opposers': opposers,
            'primary_sponsor': primary_sponsor,
        })

    context = {'legislators_stats': legislators_stats, 'bill_stats': bill_stats}
    return render(request, 'all_stats.html', context)