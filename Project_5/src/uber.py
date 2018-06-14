import pandas as pd
import numpy as np
import json


DIR = '../data/'
CVS = 'san_francisco-censustracts-2017-4-All-MonthlyAggregate.csv'
GEO = 'san_francisco_censustracts.json'
OUT = '../output/'


class location:
    def __init__(self, movement_id, name, coordinates):
        self.id = movement_id
        self.name = name
        self.coordinates = coordinates
        

def travelInDec(csv_name=CVS):
    history = pd.read_csv(DIR + csv_name)
    history = history[history.month==12]
    return history


def getLoc(json_name=GEO):
    f = open(DIR + json_name, 'r')
    geofile = json.load(f)
    f.close()
    loc_list = {}  # movement_id : location objs
    for loc_feature in geofile['features']:
        movement_id = int(loc_feature['properties']["MOVEMENT_ID"])
        name = loc_feature['properties']["DISPLAY_NAME"]
        coor = loc_feature["geometry"]["coordinates"][0][0]
        coordinates = []  # list of arrays
        for xy in coor:
            coordinates.append(np.array(xy))
        if movement_id in loc_list:
            pass
        else:
            loc_list[movement_id] = location(movement_id, name, coordinates)
    return loc_list


def write_edge_list(history):
    edge_list = {}   # node pair : travel time
    for row in history.itertuples():
        sourceid = row[1]
        dstid = row[2]
        mean_travel_time = row[4]
        pair1 = (sourceid, dstid)
        pair2 = (dstid, sourceid)
        if pair1 in edge_list:
            edge_list[pair1].append(mean_travel_time)
            # temp = edge_list[pair1]
            # edge_list[pair1] = np.mean([temp, mean_travel_time])
        elif pair2 in edge_list:
            edge_list[pair2].append(mean_travel_time)
            # temp = edge_list[pair2]
            # edge_list[pair2] = np.mean([temp, mean_travel_time])
        else:
            edge_list[pair1] = [mean_travel_time]
    for k, v in edge_list.items():
        edge_list[k] = sum(v) / float(len(v))
    with open(OUT + 'edge_list.txt', 'w+') as f:
        for pair in edge_list:
            f.write('%d\t%d\t%.3f\n'%(pair[0], pair[1], edge_list[pair]))
    return edge_list


def write_feat_list(loc_list, edge_list):
    with open(OUT + 'feat_list.txt', 'w+') as f:
        f.write('movement_id|name|coordinate\n')
    node_dict = {}  # movement_id : properties
    for pair in edge_list:
        movement_id_1 = pair[0]
        movement_id_2 = pair[1]
        name_1 = loc_list[movement_id_1].name
        coordinates = loc_list[movement_id_1].coordinates
        loc_1 = np.mean(coordinates, axis=0).tolist()
        name_2 = loc_list[movement_id_2].name
        coordinates = loc_list[movement_id_2].coordinates
        loc_2 = np.mean(coordinates, axis=0).tolist()
        if movement_id_1 in node_dict:
            pass
        else:
            node_dict[movement_id_1] = [name_1, loc_1]
        if movement_id_2 in node_dict:
            pass
        else:
            node_dict[movement_id_2] = [name_2, loc_2]
    with open(OUT + 'feat_list.txt', 'a') as f:
        for movement_id in node_dict:
            name = node_dict[movement_id][0]
            loc = node_dict[movement_id][1]
            f.write('%d|%s|%.2f,%.2f\n' % (
                movement_id, name, loc[0], loc[1]))


def main():
    history = travelInDec()
    loc_list = getLoc()
    edge_list = write_edge_list(history)
    write_feat_list(loc_list, edge_list)
    

if __name__ == '__main__':
    main()
