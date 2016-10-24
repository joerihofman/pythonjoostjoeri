class Item:
    
    total_items = 0

    def __init__(self, title, playing_time, got_it = 'N'):
        self.title = title
        self.playing_time = playing_time
        self.got_it = got_it

    def __repr__(self):
        return 'Item: %s, %s' % (self.title, self.got_it)

    def inc_total_items(self):
        global total_items
        if (self.title == None):
            total_items =+ 0
        else:
            total_items =+ 1

    inc_total_items()

class CD(Item):
    def __init__(self, title, artist, playing_time, nr_tracks, got_it = 'N'):
        self.title = title
        self.artist = artist
        self.playing_timeh = playing_time/60
        self.playing_timem = playing_time%60
        self.nr_tracks = nr_tracks
        self.got_it = got_it
    def __repr__(self):
        return 'CD: %s, %s, %i, %i %i, %s' % (self.title, self.artist, self.playing_timeh, self.playing_timem, self.nr_tracks, self.got_it)

class DVD(Item):
    def __init__(self, title, director, playing_time, nr_scenes, got_it = 'N'):
        self.title = title
        self.director = director
        self.playing_timeh = playing_time / 60
        self.playing_timem = playing_time % 60
        self.nr_scenes = nr_scenes
        self.got_it = got_it
    def __repr__(self):
        return 'CD: %s, %s, %i, %i %i, %s' % (self.title, self.director, self.playing_timeh, self.playing_timem, self.nr_scenes, self.got_it)

# stop 4 items in een lijst
my_collection = []
my_collection.append(CD('Naturally', 'JJ Cale', 80, 10, 'Y'))
my_collection.append(CD('Dire Strait', 'Dire Strait', 70, 10, 'Y'))
my_collection.append(DVD('Zodiac', 'David Fincher', 90, 10, 'N'))
my_collection.append(DVD('2001', 'Stanley Kubrick', 90, 10, 'N'))

for i in my_collection:
    print(i)
   
# laat met assert zien dat de lengte van de lijst klopt met de waarde in total_items
