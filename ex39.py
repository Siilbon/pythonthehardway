#things = ['a', 'b', 'c', 'd']
#print things[1]
#
#things[1] = 'z'
#print things[1]
#
#print things
#
#stuff = {'name': 'Zed', 'age': 39, 'height': 6 * 12 + 2}
#print stuff['name']
#
#print stuff ['age']
#
#print stuff ['height']
#
#stuff['city'] = "San Francisco"
#print stuff['city']

#stuff[1] = "Wow"
#stuff[2] = "Neato"
#print stuff[1]
#
#print stuff[2]
#
#print stuff

states = {
    'Oregan' : 'OR',
    'Florida' : 'FL',
    'California' : 'CA',
    'New York' : 'NY',
    'Michigan' : 'MI'
}


cities = {
    'CA' : 'San Fransisco',
    'MI' : 'Detroit',
    'FL' : 'Jacksonville'
}

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

print '-' * 10
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']

print '-' * 10
print "Michigan's abbrev is: ", states['Michigan']
print "Florida's abbrev is: ", states['Florida']

print '-' * 10
print "Michigan has: ", cities[states["Michigan"]]
print "Florida has: ", cities[states["Florida"]]

print '-' * 10
for state, abbrev in states.items():
    print "%s is abbrev as %s" % (state, abbrev)

print '-' * 10
for abbrev, city in cities.items():
    print "%s has the city %s" % (abbrev, city)

print '-' * 10
for state, abbrev in states.items():
    print"%s state is abbreviated %s and has city %s" % (
        state, abbrev, cities[abbrev])

print '-' * 10
state = states.get('Texas')

if not state:
    print "Sorry, not found."

city = cities.get('TX', 'Does Not Exist')
print "The city for the state 'TX' is: %s" % city
