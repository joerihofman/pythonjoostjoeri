class Item:

    total_items = 0

    @classmethod
    def inc_total_items(cls):
        global total_items
        total_items += 1
        return total_items

    def __init__(self, title, playing_time, got_it = 'N'):
        self.title = title
        self.playing_time = playing_time
        self.got_it = got_it
        Item.inc_total_items()



    def __repr__(self):
        return 'Item: %s, %s' % (self.title, self.got_it)

class CD(Item):
    def __init__(self,title,artist,playing_time,nr_tracks,got_it):
        Item.__init__(self,title,playing_time,got_it)
        self.artist=artist
        self.playing_time=playing_time
        self.nr_tracks=nr_tracks

    def __repr__(self):
        #self.palying_time
        print(self.title,self.artist,self.playing_time,self.got_it)

class DVD(Item):
    def __init__(self,title,director,playing_time,nr_scenes,got_it):
        Item.__init__(self,title,playing_time,got_it)
        self.director=director
        self.nr_scenes=nr_scenes

    def __repr__(self):
        #self.playing_time
        print(self.title,self.director,self.playing_time,self.got_it)


# stop 4 items in een lijst
my_collection = []
my_collection.append(CD('Naturally', 'JJ Cale', 80, 10, 'Y'))
my_collection.append(CD('Dire Strait', 'Dire Strait', 70, 10, 'Y'))
my_collection.append(DVD('Zodiac', 'David Fincher', 90, 10, 'N'))
my_collection.append(DVD('2001', 'Stanley Kubrick', 90, 10, 'N'))

for i in my_collection:
    print(i)
   
# laat met assert zien dat de lengte van de lijst klopt met de waarde in total_items
