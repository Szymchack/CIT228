trips = {
    'T1':{
        'type':'Cruise',
        'title': 'Grand European Tour',
        'country':'Hungry, Austria, Germany and The Netherlands',
        'cost':'3899',
    },

    'T2':{
        'type':'Cruise',
        'title': 'Journey to the Holy Land',
        'country':'Rome, Naples, Ionian Sea, Crete and the Isles',
        'cost':'3899',
    },

    'T3':{
        'type':'Cruise',
        'title':'Mediterranean Mosiac',
        'country':'Greece, Italy, France, Spain',
        'cost':'3999',
    },
}
for trip, info in trips.items():
    print(f"\nTrip:{info['type']}")
    title=info['title']
    country = info['country']
    cost = info['cost']

    print(f"\tTitle:{title}")
    print(f"\tCountry:{country}")
    print(f"\tCost: ${cost}")
