import configparser
import mysql.connector
from mysql.connector import Error


def getConfig():
    config = configparser.ConfigParser()
    config.read("utilities/properties.ini")
    return config


def getPassword():
    return 'Vinod@1007'


connect_config_dict = {
    'user': getConfig()['SQL']['user'],
    'password': getConfig()['SQL']['password'],
    'host': getConfig()['SQL']['host'],
    'database': getConfig()['SQL']['database']
}  ##-- Created dictionary for passing SQL connection values


def getConnection():
    try:
        conn = mysql.connector.connect(**connect_config_dict)  ##-- ** is to inform that data should be picked from dict
        if conn.is_connected():
            print("Connection is successful")
            return conn

    except Error as e:
        print(e)


def getQuery(query):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute(query)
    row = cursor.fetchone()
    conn.close()
    return row
