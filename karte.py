import xmltodict
import json
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import zipfile
import os
np.set_printoptions(suppress=True)

"""
This tool reads some of the data from the Finnish National Survey GML dataset and plots it with pyplot
"""

def points_from_string(input_string):
    points = np.array([float(x) for x in input_string.split(' ')])
    
def get_xml(leaf_id):
    #set this path where you have extracted the maastotietokanta
    PATH = 'C:\\datasets\\finland\\gml'
    filename = os.path.join(PATH,leaf_id[:2],leaf_id[:3],leaf_id+'_mtk.zip')
    with zipfile.ZipFile(filename) as myzip:
        with myzip.open(leaf_id+'.xml') as myfile:
            return myfile.read()

def convert_into_nparray(text):
    points = text
    points = np.array([float(x) for x in points.split(' ')])
    points = np.reshape(points,[-1,3])
    return points
    
xml_text = get_xml('L23341')
#xml_text = get_xml('P33342')
print(len(xml_text))

json_data = xmltodict.parse(xml_text)['Maastotiedot']

def get_data_list(key1, key2):
    data = json_data[key1]
    if data is None:
        return []
    data = data[key2]
    if type(data) != list:
        return [data]
    return data

data = get_data_list('tieviivat','Tieviiva')
for val in data:
    points = convert_into_nparray(val['sijainti']['Murtoviiva']['gml:posList']['#text'])
    plt.plot(points[:,0],points[:,1],'r-')

data = get_data_list('rautatiet','Rautatie')
for val in data:
    points = convert_into_nparray(val['sijainti']['Murtoviiva']['gml:posList']['#text'])
    plt.plot(points[:,0],points[:,1],'k-')

data = get_data_list('virtavesiKapeat', 'VirtavesiKapea')
for val in data:
    points = convert_into_nparray(val['sijainti']['Murtoviiva']['gml:posList']['#text'])
    plt.plot(points[:,0],points[:,1],'b-')
    
data = get_data_list('virtavesiAlueet', 'VirtavesiAlue')
for val in data:
    points = convert_into_nparray(val['sijainti']['Piste']["gml:pos"]['#text'])
    plt.plot(points[:,0],points[:,1],'b.')
    points = convert_into_nparray(val['sijainti']['Alue']["gml:exterior"]['gml:LinearRing']['gml:posList']['#text'])
    plt.plot(points[:,0],points[:,1],'b-')

data = get_data_list('jarvet','Jarvi')
for val in data:
    points = convert_into_nparray(val['sijainti']['Piste']["gml:pos"]['#text'])
    plt.plot(points[:,0],points[:,1],'b.')
    points = convert_into_nparray(val['sijainti']['Alue']["gml:exterior"]['gml:LinearRing']['gml:posList']['#text'])
    plt.plot(points[:,0],points[:,1],'b-')
    
data = get_data_list('meret','Meri')
for val in data:
    points = convert_into_nparray(val['sijainti']['Piste']["gml:pos"]['#text'])
    plt.plot(points[:,0],points[:,1],'b.')
    points = convert_into_nparray(val['sijainti']['Alue']["gml:exterior"]['gml:LinearRing']['gml:posList']['#text'])
    plt.plot(points[:,0],points[:,1],'b-')

data = get_data_list('autoliikennealueet','Autoliikennealue')
for val in data:
    points = convert_into_nparray(val['sijainti']['Piste']["gml:pos"]['#text'])
    plt.plot(points[:,0],points[:,1],'g.')
    points = convert_into_nparray(val['sijainti']['Alue']["gml:exterior"]['gml:LinearRing']['gml:posList']['#text'])
    plt.plot(points[:,0],points[:,1],'b-')

data = get_data_list('rakennukset','Rakennus')
for val in data:
    points = convert_into_nparray(val['sijainti']['Piste']["gml:pos"]['#text'])
    plt.plot(points[:,0],points[:,1],'g.')
    points = convert_into_nparray(val['sijainti']['Alue']["gml:exterior"]['gml:LinearRing']['gml:posList']['#text'])
    plt.plot(points[:,0],points[:,1],'g-')

plt.show()