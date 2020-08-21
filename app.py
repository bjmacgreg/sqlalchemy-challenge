# 1. import Flask
from flask import Flask, jsonify

# Dictionary of Precipitation
busiest_station_prcp_dict = [
    {'date': '2016-08-24', 'prcp': 2.15}
    {'date': '2016-08-25', 'prcp': 0.06}
    {'date': '2016-08-26', 'prcp': 0.01}
    {'date': '2016-08-27', 'prcp': 0.12}
    {'date': '2016-08-28', 'prcp': 0.6}
    {'date': '2016-08-29', 'prcp': 0.35}
    {'date': '2016-08-30', 'prcp': 0.0}
    {'date': '2016-08-31', 'prcp': 0.24}
    {'date': '2016-09-01', 'prcp': 0.02}
    {'date': '2016-09-02', 'prcp': 0.01}
    {'date': '2016-09-03', 'prcp': 0.12}
    {'date': '2016-09-04', 'prcp': 0.14}
    {'date': '2016-09-05', 'prcp': 0.03}
    {'date': '2016-09-06', 'prcp': 0.11}
    {'date': '2016-09-07', 'prcp': 0.16}
    {'date': '2016-09-08', 'prcp': 0.07}
    {'date': '2016-09-09', 'prcp': 0.16}
    {'date': '2016-09-10', 'prcp': 0.09}
    {'date': '2016-09-11', 'prcp': 0.3}
    {'date': '2016-09-12', 'prcp': 0.31}
    {'date': '2016-09-13', 'prcp': 0.34}
    {'date': '2016-09-14', 'prcp': 2.33}
    {'date': '2016-09-15', 'prcp': 0.83}
    {'date': '2016-09-16', 'prcp': 0.06}
    {'date': '2016-09-17', 'prcp': 0.36}
    {'date': '2016-09-18', 'prcp': 0.07}
    {'date': '2016-09-19', 'prcp': 0.01}
    {'date': '2016-09-20', 'prcp': 0.22}
    {'date': '2016-09-21', 'prcp': 0.07}
    {'date': '2016-09-22', 'prcp': 0.34}
    {'date': '2016-09-23', 'prcp': 0.94}
    {'date': '2016-09-24', 'prcp': 0.01}
    {'date': '2016-09-25', 'prcp': 0.03}
    {'date': '2016-09-26', 'prcp': 0.17}
    {'date': '2016-09-27', 'prcp': 0.17}
    {'date': '2016-09-28', 'prcp': 0.0}
    {'date': '2016-09-29', 'prcp': 0.59}
    {'date': '2016-09-30', 'prcp': 0.25}
    {'date': '2016-10-01', 'prcp': 0.14}
    {'date': '2016-10-02', 'prcp': 0.06}
    {'date': '2016-10-03', 'prcp': 0.16}
    {'date': '2016-10-04', 'prcp': 0.03}
    {'date': '2016-10-05', 'prcp': 0.01}
    {'date': '2016-10-06', 'prcp': 0.0}
    {'date': '2016-10-07', 'prcp': 0.0}
    {'date': '2016-10-08', 'prcp': 0.0}
    {'date': '2016-10-09', 'prcp': 0.0}
    {'date': '2016-10-10', 'prcp': 0.0}
    {'date': '2016-10-11', 'prcp': 0.28}
    {'date': '2016-10-12', 'prcp': 0.03}
    {'date': '2016-10-13', 'prcp': 0.0}
    {'date': '2016-10-14', 'prcp': 0.0}
    {'date': '2016-10-15', 'prcp': 0.04}
    {'date': '2016-10-16', 'prcp': 0.0}
    {'date': '2016-10-17', 'prcp': 0.01}
    {'date': '2016-10-18', 'prcp': 0.02}
    {'date': '2016-10-19', 'prcp': 0.11}
    {'date': '2016-10-20', 'prcp': 0.0}
    {'date': '2016-10-21', 'prcp': 0.0}
    {'date': '2016-10-22', 'prcp': 0.15}
    {'date': '2016-10-23', 'prcp': 0.02}
    {'date': '2016-10-24', 'prcp': 0.08}
    {'date': '2016-10-25', 'prcp': 0.11}
    {'date': '2016-10-26', 'prcp': 0.01}
    {'date': '2016-10-27', 'prcp': 0.22}
    {'date': '2016-10-28', 'prcp': 0.05}
    {'date': '2016-10-29', 'prcp': 0.1}
    {'date': '2016-10-30', 'prcp': 0.16}
    {'date': '2016-10-31', 'prcp': 0.07}
    {'date': '2016-11-01', 'prcp': 0.1}
    {'date': '2016-11-02', 'prcp': 0.0}
    {'date': '2016-11-03', 'prcp': 0.0}
    {'date': '2016-11-04', 'prcp': 0.0}
    {'date': '2016-11-05', 'prcp': 0.03}
    {'date': '2016-11-06', 'prcp': 0.01}
    {'date': '2016-11-07', 'prcp': 0.0}
    {'date': '2016-11-08', 'prcp': 0.21}
    {'date': '2016-11-09', 'prcp': 0.11}
    {'date': '2016-11-10', 'prcp': 0.0}
    {'date': '2016-11-11', 'prcp': 0.0}
    {'date': '2016-11-12', 'prcp': 0.0}
    {'date': '2016-11-13', 'prcp': 0.0}
    {'date': '2016-11-14', 'prcp': 0.0}
    {'date': '2016-11-15', 'prcp': 0.0}
    {'date': '2016-11-16', 'prcp': 0.24}
    {'date': '2016-11-17', 'prcp': 0.01}
    {'date': '2016-11-18', 'prcp': 0.0}
    {'date': '2016-11-19', 'prcp': 0.11}
    {'date': '2016-11-20', 'prcp': 0.39}
    {'date': '2016-11-21', 'prcp': 0.11}
    {'date': '2016-11-22', 'prcp': 2.05}
    {'date': '2016-11-23', 'prcp': 0.25}
    {'date': '2016-11-24', 'prcp': 0.3}
    {'date': '2016-11-25', 'prcp': 0.08}
    {'date': '2016-11-26', 'prcp': 0.06}
    {'date': '2016-11-27', 'prcp': 0.17}
    {'date': '2016-11-28', 'prcp': 0.0}
    {'date': '2016-11-29', 'prcp': 0.09}
    {'date': '2016-11-30', 'prcp': 0.05}
    {'date': '2016-12-01', 'prcp': 0.37}
    {'date': '2016-12-02', 'prcp': 0.35}
    {'date': '2016-12-03', 'prcp': 0.77}
    {'date': '2016-12-04', 'prcp': 0.04}
    {'date': '2016-12-05', 'prcp': 0.22}
    {'date': '2016-12-06', 'prcp': 0.0}
    {'date': '2016-12-07', 'prcp': 0.12}
    {'date': '2016-12-08', 'prcp': 0.07}
    {'date': '2016-12-09', 'prcp': 0.31}
    {'date': '2016-12-10', 'prcp': 0.02}
    {'date': '2016-12-11', 'prcp': 0.0}
    {'date': '2016-12-12', 'prcp': 0.0}
    {'date': '2016-12-13', 'prcp': 0.04}
    {'date': '2016-12-14', 'prcp': 0.92}
    {'date': '2016-12-15', 'prcp': 0.14}
    {'date': '2016-12-16', 'prcp': 0.03}
    {'date': '2016-12-17', 'prcp': 0.07}
    {'date': '2016-12-18', 'prcp': 0.16}
    {'date': '2016-12-19', 'prcp': 0.03}
    {'date': '2016-12-20', 'prcp': 0.0}
    {'date': '2016-12-21', 'prcp': 0.11}
    {'date': '2016-12-22', 'prcp': 0.86}
    {'date': '2016-12-23', 'prcp': 0.24}
    {'date': '2016-12-24', 'prcp': 0.2}
    {'date': '2016-12-25', 'prcp': 0.02}
    {'date': '2016-12-26', 'prcp': 0.22}
    {'date': '2016-12-27', 'prcp': 0.05}
    {'date': '2016-12-28', 'prcp': 0.09}
    {'date': '2016-12-29', 'prcp': 0.52}
    {'date': '2016-12-30', 'prcp': 0.29}
    {'date': '2016-12-31', 'prcp': 0.25}
    {'date': '2017-01-01', 'prcp': 0.03}
    {'date': '2017-01-02', 'prcp': 0.01}
    {'date': '2017-01-03', 'prcp': 0.0}
    {'date': '2017-01-04', 'prcp': 0.0}
    {'date': '2017-01-05', 'prcp': 0.06}
    {'date': '2017-01-06', 'prcp': 0.1}
    {'date': '2017-01-07', 'prcp': 0.0}
    {'date': '2017-01-08', 'prcp': 0.0}
    {'date': '2017-01-09', 'prcp': 0.0}
    {'date': '2017-01-10', 'prcp': 0.0}
    {'date': '2017-01-11', 'prcp': 0.0}
    {'date': '2017-01-12', 'prcp': 0.0}
    {'date': '2017-01-13', 'prcp': 0.0}
    {'date': '2017-01-14', 'prcp': 0.01}
    {'date': '2017-01-15', 'prcp': 0.0}
    {'date': '2017-01-16', 'prcp': 0.0}
    {'date': '2017-01-17', 'prcp': 0.0}
    {'date': '2017-01-18', 'prcp': 0.0}
    {'date': '2017-01-19', 'prcp': 0.02}
    {'date': '2017-01-20', 'prcp': 0.0}
    {'date': '2017-01-21', 'prcp': 0.03}
    {'date': '2017-01-22', 'prcp': 0.09}
    {'date': '2017-01-23', 'prcp': 0.01}
    {'date': '2017-01-24', 'prcp': 0.13}
    {'date': '2017-01-25', 'prcp': 0.79}
    {'date': '2017-01-26', 'prcp': 0.0}
    {'date': '2017-01-27', 'prcp': 0.03}
    {'date': '2017-01-28', 'prcp': 0.0}
    {'date': '2017-01-29', 'prcp': 0.26}
    {'date': '2017-01-30', 'prcp': 0.0}
    {'date': '2017-01-31', 'prcp': 0.0}
    {'date': '2017-02-01', 'prcp': 0.0}
    {'date': '2017-02-02', 'prcp': 0.0}
    {'date': '2017-02-03', 'prcp': 0.0}
    {'date': '2017-02-04', 'prcp': 0.0}
    {'date': '2017-02-05', 'prcp': 0.0}
    {'date': '2017-02-06', 'prcp': 0.18}
    {'date': '2017-02-07', 'prcp': 1.32}
    {'date': '2017-02-08', 'prcp': 0.0}
    {'date': '2017-02-09', 'prcp': 0.0}
    {'date': '2017-02-10', 'prcp': 0.0}
    {'date': '2017-02-11', 'prcp': 1.73}
    {'date': '2017-02-12', 'prcp': 2.98}
    {'date': '2017-02-13', 'prcp': 0.01}
    {'date': '2017-02-14', 'prcp': 0.0}
    {'date': '2017-02-15', 'prcp': 0.01}
    {'date': '2017-02-16', 'prcp': 0.73}
    {'date': '2017-02-17', 'prcp': 0.13}
    {'date': '2017-02-18', 'prcp': 0.0}
    {'date': '2017-02-19', 'prcp': 0.09}
    {'date': '2017-02-20', 'prcp': 0.0}
    {'date': '2017-02-21', 'prcp': 0.0}
    {'date': '2017-02-22', 'prcp': 0.06}
    {'date': '2017-02-23', 'prcp': 0.0}
    {'date': '2017-02-24', 'prcp': 0.0}
    {'date': '2017-02-25', 'prcp': 0.0}
    {'date': '2017-02-26', 'prcp': 0.0}
    {'date': '2017-02-27', 'prcp': 0.0}
    {'date': '2017-02-28', 'prcp': 0.04}
    {'date': '2017-03-01', 'prcp': 2.12}
    {'date': '2017-03-02', 'prcp': 1.88}
    {'date': '2017-03-03', 'prcp': 0.27}
    {'date': '2017-03-04', 'prcp': 0.0}
    {'date': '2017-03-05', 'prcp': 0.41}
    {'date': '2017-03-06', 'prcp': 0.03}
    {'date': '2017-03-07', 'prcp': 0.0}
    {'date': '2017-03-08', 'prcp': 0.0}
    {'date': '2017-03-09', 'prcp': 0.65}
    {'date': '2017-03-10', 'prcp': 0.03}
    {'date': '2017-03-11', 'prcp': 0.01}
    {'date': '2017-03-12', 'prcp': 0.0}
    {'date': '2017-03-13', 'prcp': 0.0}
    {'date': '2017-03-14', 'prcp': 0.0}
    {'date': '2017-03-15', 'prcp': 0.06}
    {'date': '2017-03-16', 'prcp': 0.0}
    {'date': '2017-03-17', 'prcp': 0.12}
    {'date': '2017-03-18', 'prcp': 0.0}
    {'date': '2017-03-19', 'prcp': 0.0}
    {'date': '2017-03-20', 'prcp': 0.02}
    {'date': '2017-03-21', 'prcp': 0.09}
    {'date': '2017-03-22', 'prcp': 0.0}
    {'date': '2017-03-23', 'prcp': 0.0}
    {'date': '2017-03-24', 'prcp': 0.12}
    {'date': '2017-03-25', 'prcp': 0.93}
    {'date': '2017-03-26', 'prcp': 0.0}
    {'date': '2017-03-27', 'prcp': 0.01}
    {'date': '2017-03-28', 'prcp': 0.0}
    {'date': '2017-03-29', 'prcp': 0.01}
    {'date': '2017-03-30', 'prcp': 0.04}
    {'date': '2017-03-31', 'prcp': 0.01}
    {'date': '2017-04-01', 'prcp': 0.21}
    {'date': '2017-04-02', 'prcp': 0.0}
    {'date': '2017-04-03', 'prcp': 0.26}
    {'date': '2017-04-04', 'prcp': 0.09}
    {'date': '2017-04-05', 'prcp': 0.1}
    {'date': '2017-04-06', 'prcp': 0.06}
    {'date': '2017-04-07', 'prcp': 0.0}
    {'date': '2017-04-08', 'prcp': 0.0}
    {'date': '2017-04-09', 'prcp': 0.0}
    {'date': '2017-04-10', 'prcp': 0.01}
    {'date': '2017-04-11', 'prcp': 0.03}
    {'date': '2017-04-12', 'prcp': 0.11}
    {'date': '2017-04-13', 'prcp': 0.59}
    {'date': '2017-04-14', 'prcp': 2.3}
    {'date': '2017-04-15', 'prcp': 0.38}
    {'date': '2017-04-16', 'prcp': 0.47}
    {'date': '2017-04-17', 'prcp': 1.04}
    {'date': '2017-04-18', 'prcp': 2.03}
    {'date': '2017-04-19', 'prcp': 0.02}
    {'date': '2017-04-20', 'prcp': 0.05}
    {'date': '2017-04-21', 'prcp': 1.74}
    {'date': '2017-04-22', 'prcp': 1.58}
    {'date': '2017-04-23', 'prcp': 0.06}
    {'date': '2017-04-24', 'prcp': 0.01}
    {'date': '2017-04-25', 'prcp': 0.0}
    {'date': '2017-04-26', 'prcp': 0.02}
    {'date': '2017-04-27', 'prcp': 0.19}
    {'date': '2017-04-28', 'prcp': 0.76}
    {'date': '2017-04-29', 'prcp': 0.37}
    {'date': '2017-04-30', 'prcp': 1.04}
    {'date': '2017-05-01', 'prcp': 0.13}
    {'date': '2017-05-02', 'prcp': 0.01}
    {'date': '2017-05-03', 'prcp': 0.01}
    {'date': '2017-05-04', 'prcp': 0.0}
    {'date': '2017-05-05', 'prcp': 0.0}
    {'date': '2017-05-06', 'prcp': 0.0}
    {'date': '2017-05-07', 'prcp': 0.02}
    {'date': '2017-05-08', 'prcp': 0.73}
    {'date': '2017-05-09', 'prcp': 1.58}
    {'date': '2017-05-10', 'prcp': 0.2}
    {'date': '2017-05-11', 'prcp': 0.12}
    {'date': '2017-05-12', 'prcp': 0.02}
    {'date': '2017-05-13', 'prcp': 0.12}
    {'date': '2017-05-14', 'prcp': 0.17}
    {'date': '2017-05-15', 'prcp': 0.09}
    {'date': '2017-05-16', 'prcp': 0.03}
    {'date': '2017-05-17', 'prcp': 0.07}
    {'date': '2017-05-18', 'prcp': 0.13}
    {'date': '2017-05-19', 'prcp': 0.01}
    {'date': '2017-05-20', 'prcp': 0.02}
    {'date': '2017-05-21', 'prcp': 0.01}
    {'date': '2017-05-22', 'prcp': 0.06}
    {'date': '2017-05-23', 'prcp': 0.06}
    {'date': '2017-05-24', 'prcp': 0.3}
    {'date': '2017-05-25', 'prcp': 0.2}
    {'date': '2017-05-26', 'prcp': 0.0}
    {'date': '2017-05-27', 'prcp': 0.0}
    {'date': '2017-05-28', 'prcp': 0.08}
    {'date': '2017-05-29', 'prcp': 0.4}
    {'date': '2017-05-30', 'prcp': 1.12}
    {'date': '2017-05-31', 'prcp': 0.25}
    {'date': '2017-06-01', 'prcp': 0.0}
    {'date': '2017-06-02', 'prcp': 0.09}
    {'date': '2017-06-03', 'prcp': 0.08}
    {'date': '2017-06-04', 'prcp': 0.13}
    {'date': '2017-06-05', 'prcp': 0.05}
    {'date': '2017-06-06', 'prcp': 0.0}
    {'date': '2017-06-07', 'prcp': 0.0}
    {'date': '2017-06-08', 'prcp': 0.0}
    {'date': '2017-06-09', 'prcp': 0.02}
    {'date': '2017-06-10', 'prcp': 0.62}
    {'date': '2017-06-11', 'prcp': 0.74}
    {'date': '2017-06-12', 'prcp': 0.24}
    {'date': '2017-06-13', 'prcp': 0.24}
    {'date': '2017-06-14', 'prcp': 0.22}
    {'date': '2017-06-15', 'prcp': 0.55}
    {'date': '2017-06-16', 'prcp': 0.06}
    {'date': '2017-06-17', 'prcp': 0.07}
    {'date': '2017-06-18', 'prcp': 0.24}
    {'date': '2017-06-19', 'prcp': 0.08}
    {'date': '2017-06-20', 'prcp': 0.0}
    {'date': '2017-06-21', 'prcp': 0.19}
    {'date': '2017-06-22', 'prcp': 0.06}
    {'date': '2017-06-23', 'prcp': 0.12}
    {'date': '2017-06-24', 'prcp': 0.36}
    {'date': '2017-06-25', 'prcp': 0.02}
    {'date': '2017-06-26', 'prcp': 0.06}
    {'date': '2017-06-27', 'prcp': 0.01}
    {'date': '2017-06-28', 'prcp': 0.0}
    {'date': '2017-06-29', 'prcp': 0.0}
    {'date': '2017-06-30', 'prcp': 0.01}
    {'date': '2017-07-01', 'prcp': 0.08}
    {'date': '2017-07-02', 'prcp': 0.15}
    {'date': '2017-07-03', 'prcp': 0.15}
    {'date': '2017-07-04', 'prcp': 0.08}
    {'date': '2017-07-05', 'prcp': 0.0}
    {'date': '2017-07-06', 'prcp': 0.0}
    {'date': '2017-07-07', 'prcp': 0.18}
    {'date': '2017-07-08', 'prcp': 0.0}
    {'date': '2017-07-09', 'prcp': 0.11}
    {'date': '2017-07-10', 'prcp': 0.02}
    {'date': '2017-07-11', 'prcp': 0.02}
    {'date': '2017-07-12', 'prcp': 0.28}
    {'date': '2017-07-13', 'prcp': 0.32}
    {'date': '2017-07-14', 'prcp': 0.2}
    {'date': '2017-07-15', 'prcp': 0.05}
    {'date': '2017-07-16', 'prcp': 0.1}
    {'date': '2017-07-17', 'prcp': 0.21}
    {'date': '2017-07-18', 'prcp': 0.05}
    {'date': '2017-07-19', 'prcp': 0.05}
    {'date': '2017-07-20', 'prcp': 0.06}
    {'date': '2017-07-21', 'prcp': 0.03}
    {'date': '2017-07-22', 'prcp': 0.2}
    {'date': '2017-07-23', 'prcp': 0.2}
    {'date': '2017-07-24', 'prcp': 0.61}
    {'date': '2017-07-25', 'prcp': 0.11}
    {'date': '2017-07-26', 'prcp': 0.12}
    {'date': '2017-07-27', 'prcp': 0.01}
    {'date': '2017-07-28', 'prcp': 0.09}
    {'date': '2017-07-29', 'prcp': 0.23}
    {'date': '2017-07-30', 'prcp': 0.0}
    {'date': '2017-07-31', 'prcp': 0.0}
    {'date': '2017-08-04', 'prcp': 0.0}
    {'date': '2017-08-05', 'prcp': 0.06}
    {'date': '2017-08-06', 'prcp': 0.0}
    {'date': '2017-08-13', 'prcp': 0.0}
    {'date': '2017-08-14', 'prcp': 0.0}
    {'date': '2017-08-15', 'prcp': 0.32}
    {'date': '2017-08-16', 'prcp': 0.12}
    {'date': '2017-08-17', 'prcp': 0.01}
    {'date': '2017-08-18', 'prcp': 0.06}
]
# Dictionary of Temperature
busiest_station_tobs_dict = [
    {'date': '2016-08-24', 'tobs': 77.0}
    {'date': '2016-08-25', 'tobs': 80.0}
    {'date': '2016-08-26', 'tobs': 80.0}
    {'date': '2016-08-27', 'tobs': 75.0}
    {'date': '2016-08-28', 'tobs': 73.0}
    {'date': '2016-08-29', 'tobs': 78.0}
    {'date': '2016-08-30', 'tobs': 77.0}
    {'date': '2016-08-31', 'tobs': 78.0}
    {'date': '2016-09-01', 'tobs': 80.0}
    {'date': '2016-09-02', 'tobs': 80.0}
    {'date': '2016-09-03', 'tobs': 78.0}
    {'date': '2016-09-04', 'tobs': 78.0}
    {'date': '2016-09-05', 'tobs': 78.0}
    {'date': '2016-09-06', 'tobs': 73.0}
    {'date': '2016-09-07', 'tobs': 74.0}
    {'date': '2016-09-08', 'tobs': 80.0}
    {'date': '2016-09-09', 'tobs': 79.0}
    {'date': '2016-09-10', 'tobs': 77.0}
    {'date': '2016-09-11', 'tobs': 80.0}
    {'date': '2016-09-12', 'tobs': 76.0}
    {'date': '2016-09-13', 'tobs': 79.0}
    {'date': '2016-09-14', 'tobs': 75.0}
    {'date': '2016-09-15', 'tobs': 79.0}
    {'date': '2016-09-16', 'tobs': 78.0}
    {'date': '2016-09-17', 'tobs': 79.0}
    {'date': '2016-09-18', 'tobs': 78.0}
    {'date': '2016-09-19', 'tobs': 78.0}
    {'date': '2016-09-20', 'tobs': 76.0}
    {'date': '2016-09-21', 'tobs': 74.0}
    {'date': '2016-09-22', 'tobs': 77.0}
    {'date': '2016-09-23', 'tobs': 78.0}
    {'date': '2016-09-24', 'tobs': 79.0}
    {'date': '2016-09-25', 'tobs': 79.0}
    {'date': '2016-09-26', 'tobs': 77.0}
    {'date': '2016-09-27', 'tobs': 80.0}
    {'date': '2016-09-28', 'tobs': 78.0}
    {'date': '2016-09-29', 'tobs': 78.0}
    {'date': '2016-09-30', 'tobs': 78.0}
    {'date': '2016-10-01', 'tobs': 77.0}
    {'date': '2016-10-02', 'tobs': 79.0}
    {'date': '2016-10-03', 'tobs': 79.0}
    {'date': '2016-10-04', 'tobs': 79.0}
    {'date': '2016-10-05', 'tobs': 79.0}
    {'date': '2016-10-06', 'tobs': 75.0}
    {'date': '2016-10-07', 'tobs': 76.0}
    {'date': '2016-10-08', 'tobs': 73.0}
    {'date': '2016-10-09', 'tobs': 72.0}
    {'date': '2016-10-10', 'tobs': 71.0}
    {'date': '2016-10-11', 'tobs': 77.0}
    {'date': '2016-10-12', 'tobs': 79.0}
    {'date': '2016-10-13', 'tobs': 78.0}
    {'date': '2016-10-14', 'tobs': 79.0}
    {'date': '2016-10-15', 'tobs': 77.0}
    {'date': '2016-10-16', 'tobs': 79.0}
    {'date': '2016-10-17', 'tobs': 77.0}
    {'date': '2016-10-18', 'tobs': 78.0}
    {'date': '2016-10-19', 'tobs': 78.0}
    {'date': '2016-10-20', 'tobs': 78.0}
    {'date': '2016-10-21', 'tobs': 78.0}
    {'date': '2016-10-22', 'tobs': 77.0}
    {'date': '2016-10-23', 'tobs': 74.0}
    {'date': '2016-10-24', 'tobs': 75.0}
    {'date': '2016-10-25', 'tobs': 76.0}
    {'date': '2016-10-26', 'tobs': 73.0}
    {'date': '2016-10-27', 'tobs': 76.0}
    {'date': '2016-10-28', 'tobs': 74.0}
    {'date': '2016-10-29', 'tobs': 77.0}
    {'date': '2016-10-30', 'tobs': 76.0}
    {'date': '2016-10-31', 'tobs': 76.0}
    {'date': '2016-11-01', 'tobs': 74.0}
    {'date': '2016-11-02', 'tobs': 75.0}
    {'date': '2016-11-03', 'tobs': 75.0}
    {'date': '2016-11-04', 'tobs': 75.0}
    {'date': '2016-11-05', 'tobs': 75.0}
    {'date': '2016-11-06', 'tobs': 71.0}
    {'date': '2016-11-07', 'tobs': 63.0}
    {'date': '2016-11-08', 'tobs': 70.0}
    {'date': '2016-11-09', 'tobs': 68.0}
    {'date': '2016-11-10', 'tobs': 67.0}
    {'date': '2016-11-11', 'tobs': 77.0}
    {'date': '2016-11-12', 'tobs': 74.0}
    {'date': '2016-11-13', 'tobs': 77.0}
    {'date': '2016-11-14', 'tobs': 76.0}
    {'date': '2016-11-15', 'tobs': 76.0}
    {'date': '2016-11-16', 'tobs': 75.0}
    {'date': '2016-11-17', 'tobs': 76.0}
    {'date': '2016-11-18', 'tobs': 75.0}
    {'date': '2016-11-19', 'tobs': 73.0}
    {'date': '2016-11-20', 'tobs': 75.0}
    {'date': '2016-11-21', 'tobs': 73.0}
    {'date': '2016-11-22', 'tobs': 75.0}
    {'date': '2016-11-23', 'tobs': 74.0}
    {'date': '2016-11-24', 'tobs': 75.0}
    {'date': '2016-11-25', 'tobs': 74.0}
    {'date': '2016-11-26', 'tobs': 75.0}
    {'date': '2016-11-27', 'tobs': 73.0}
    {'date': '2016-11-28', 'tobs': 75.0}
    {'date': '2016-11-29', 'tobs': 73.0}
    {'date': '2016-11-30', 'tobs': 73.0}
    {'date': '2016-12-01', 'tobs': 74.0}
    {'date': '2016-12-02', 'tobs': 70.0}
    {'date': '2016-12-03', 'tobs': 72.0}
    {'date': '2016-12-04', 'tobs': 70.0}
    {'date': '2016-12-05', 'tobs': 67.0}
    {'date': '2016-12-06', 'tobs': 67.0}
    {'date': '2016-12-07', 'tobs': 69.0}
    {'date': '2016-12-08', 'tobs': 70.0}
    {'date': '2016-12-09', 'tobs': 68.0}
    {'date': '2016-12-10', 'tobs': 69.0}
    {'date': '2016-12-11', 'tobs': 69.0}
    {'date': '2016-12-12', 'tobs': 66.0}
    {'date': '2016-12-13', 'tobs': 65.0}
    {'date': '2016-12-14', 'tobs': 68.0}
    {'date': '2016-12-15', 'tobs': 62.0}
    {'date': '2016-12-16', 'tobs': 75.0}
    {'date': '2016-12-17', 'tobs': 70.0}
    {'date': '2016-12-18', 'tobs': 69.0}
    {'date': '2016-12-19', 'tobs': 76.0}
    {'date': '2016-12-20', 'tobs': 76.0}
    {'date': '2016-12-21', 'tobs': 74.0}
    {'date': '2016-12-22', 'tobs': 73.0}
    {'date': '2016-12-23', 'tobs': 71.0}
    {'date': '2016-12-24', 'tobs': 74.0}
    {'date': '2016-12-25', 'tobs': 74.0}
    {'date': '2016-12-26', 'tobs': 72.0}
    {'date': '2016-12-27', 'tobs': 71.0}
    {'date': '2016-12-28', 'tobs': 72.0}
    {'date': '2016-12-29', 'tobs': 74.0}
    {'date': '2016-12-30', 'tobs': 69.0}
    {'date': '2016-12-31', 'tobs': 67.0}
    {'date': '2017-01-01', 'tobs': 72.0}
    {'date': '2017-01-02', 'tobs': 70.0}
    {'date': '2017-01-03', 'tobs': 64.0}
    {'date': '2017-01-04', 'tobs': 63.0}
    {'date': '2017-01-05', 'tobs': 63.0}
    {'date': '2017-01-06', 'tobs': 62.0}
    {'date': '2017-01-07', 'tobs': 70.0}
    {'date': '2017-01-08', 'tobs': 70.0}
    {'date': '2017-01-09', 'tobs': 62.0}
    {'date': '2017-01-10', 'tobs': 62.0}
    {'date': '2017-01-11', 'tobs': 63.0}
    {'date': '2017-01-12', 'tobs': 65.0}
    {'date': '2017-01-13', 'tobs': 69.0}
    {'date': '2017-01-14', 'tobs': 77.0}
    {'date': '2017-01-15', 'tobs': 70.0}
    {'date': '2017-01-16', 'tobs': 74.0}
    {'date': '2017-01-17', 'tobs': 69.0}
    {'date': '2017-01-18', 'tobs': 72.0}
    {'date': '2017-01-19', 'tobs': 71.0}
    {'date': '2017-01-20', 'tobs': 69.0}
    {'date': '2017-01-21', 'tobs': 71.0}
    {'date': '2017-01-22', 'tobs': 71.0}
    {'date': '2017-01-23', 'tobs': 72.0}
    {'date': '2017-01-24', 'tobs': 72.0}
    {'date': '2017-01-25', 'tobs': 69.0}
    {'date': '2017-01-26', 'tobs': 70.0}
    {'date': '2017-01-27', 'tobs': 66.0}
    {'date': '2017-01-28', 'tobs': 65.0}
    {'date': '2017-01-29', 'tobs': 69.0}
    {'date': '2017-01-30', 'tobs': 68.0}
    {'date': '2017-01-31', 'tobs': 68.0}
    {'date': '2017-02-01', 'tobs': 68.0}
    {'date': '2017-02-02', 'tobs': 59.0}
    {'date': '2017-02-03', 'tobs': 60.0}
    {'date': '2017-02-04', 'tobs': 70.0}
    {'date': '2017-02-05', 'tobs': 73.0}
    {'date': '2017-02-06', 'tobs': 75.0}
    {'date': '2017-02-07', 'tobs': 64.0}
    {'date': '2017-02-08', 'tobs': 59.0}
    {'date': '2017-02-09', 'tobs': 59.0}
    {'date': '2017-02-10', 'tobs': 62.0}
    {'date': '2017-02-11', 'tobs': 68.0}
    {'date': '2017-02-12', 'tobs': 70.0}
    {'date': '2017-02-13', 'tobs': 73.0}
    {'date': '2017-02-14', 'tobs': 79.0}
    {'date': '2017-02-15', 'tobs': 75.0}
    {'date': '2017-02-16', 'tobs': 65.0}
    {'date': '2017-02-17', 'tobs': 70.0}
    {'date': '2017-02-18', 'tobs': 74.0}
    {'date': '2017-02-19', 'tobs': 70.0}
    {'date': '2017-02-20', 'tobs': 70.0}
    {'date': '2017-02-21', 'tobs': 71.0}
    {'date': '2017-02-22', 'tobs': 71.0}
    {'date': '2017-02-23', 'tobs': 71.0}
    {'date': '2017-02-24', 'tobs': 69.0}
    {'date': '2017-02-25', 'tobs': 61.0}
    {'date': '2017-02-26', 'tobs': 67.0}
    {'date': '2017-02-27', 'tobs': 65.0}
    {'date': '2017-02-28', 'tobs': 72.0}
    {'date': '2017-03-01', 'tobs': 71.0}
    {'date': '2017-03-02', 'tobs': 73.0}
    {'date': '2017-03-03', 'tobs': 72.0}
    {'date': '2017-03-04', 'tobs': 77.0}
    {'date': '2017-03-05', 'tobs': 73.0}
    {'date': '2017-03-06', 'tobs': 67.0}
    {'date': '2017-03-07', 'tobs': 62.0}
    {'date': '2017-03-08', 'tobs': 64.0}
    {'date': '2017-03-09', 'tobs': 67.0}
    {'date': '2017-03-10', 'tobs': 66.0}
    {'date': '2017-03-11', 'tobs': 81.0}
    {'date': '2017-03-12', 'tobs': 69.0}
    {'date': '2017-03-13', 'tobs': 66.0}
    {'date': '2017-03-14', 'tobs': 67.0}
    {'date': '2017-03-15', 'tobs': 69.0}
    {'date': '2017-03-16', 'tobs': 66.0}
    {'date': '2017-03-17', 'tobs': 68.0}
    {'date': '2017-03-18', 'tobs': 65.0}
    {'date': '2017-03-19', 'tobs': 74.0}
    {'date': '2017-03-20', 'tobs': 69.0}
    {'date': '2017-03-21', 'tobs': 72.0}
    {'date': '2017-03-22', 'tobs': 73.0}
    {'date': '2017-03-23', 'tobs': 72.0}
    {'date': '2017-03-24', 'tobs': 71.0}
    {'date': '2017-03-25', 'tobs': 76.0}
    {'date': '2017-03-26', 'tobs': 77.0}
    {'date': '2017-03-27', 'tobs': 76.0}
    {'date': '2017-03-28', 'tobs': 74.0}
    {'date': '2017-03-29', 'tobs': 68.0}
    {'date': '2017-03-30', 'tobs': 73.0}
    {'date': '2017-03-31', 'tobs': 71.0}
    {'date': '2017-04-01', 'tobs': 74.0}
    {'date': '2017-04-02', 'tobs': 75.0}
    {'date': '2017-04-03', 'tobs': 70.0}
    {'date': '2017-04-04', 'tobs': 67.0}
    {'date': '2017-04-05', 'tobs': 71.0}
    {'date': '2017-04-06', 'tobs': 67.0}
    {'date': '2017-04-07', 'tobs': 74.0}
    {'date': '2017-04-08', 'tobs': 77.0}
    {'date': '2017-04-09', 'tobs': 78.0}
    {'date': '2017-04-10', 'tobs': 67.0}
    {'date': '2017-04-11', 'tobs': 70.0}
    {'date': '2017-04-12', 'tobs': 69.0}
    {'date': '2017-04-13', 'tobs': 69.0}
    {'date': '2017-04-14', 'tobs': 74.0}
    {'date': '2017-04-15', 'tobs': 78.0}
    {'date': '2017-04-16', 'tobs': 71.0}
    {'date': '2017-04-17', 'tobs': 67.0}
    {'date': '2017-04-18', 'tobs': 68.0}
    {'date': '2017-04-19', 'tobs': 67.0}
    {'date': '2017-04-20', 'tobs': 76.0}
    {'date': '2017-04-21', 'tobs': 69.0}
    {'date': '2017-04-22', 'tobs': 72.0}
    {'date': '2017-04-23', 'tobs': 76.0}
    {'date': '2017-04-24', 'tobs': 68.0}
    {'date': '2017-04-25', 'tobs': 72.0}
    {'date': '2017-04-26', 'tobs': 74.0}
    {'date': '2017-04-27', 'tobs': 70.0}
    {'date': '2017-04-28', 'tobs': 67.0}
    {'date': '2017-04-29', 'tobs': 72.0}
    {'date': '2017-04-30', 'tobs': 60.0}
    {'date': '2017-05-01', 'tobs': 65.0}
    {'date': '2017-05-02', 'tobs': 75.0}
    {'date': '2017-05-03', 'tobs': 70.0}
    {'date': '2017-05-04', 'tobs': 75.0}
    {'date': '2017-05-05', 'tobs': 70.0}
    {'date': '2017-05-06', 'tobs': 79.0}
    {'date': '2017-05-07', 'tobs': 75.0}
    {'date': '2017-05-08', 'tobs': 70.0}
    {'date': '2017-05-09', 'tobs': 67.0}
    {'date': '2017-05-10', 'tobs': 74.0}
    {'date': '2017-05-11', 'tobs': 70.0}
    {'date': '2017-05-12', 'tobs': 75.0}
    {'date': '2017-05-13', 'tobs': 76.0}
    {'date': '2017-05-14', 'tobs': 77.0}
    {'date': '2017-05-15', 'tobs': 74.0}
    {'date': '2017-05-16', 'tobs': 74.0}
    {'date': '2017-05-17', 'tobs': 74.0}
    {'date': '2017-05-18', 'tobs': 69.0}
    {'date': '2017-05-19', 'tobs': 68.0}
    {'date': '2017-05-20', 'tobs': 76.0}
    {'date': '2017-05-21', 'tobs': 74.0}
    {'date': '2017-05-22', 'tobs': 71.0}
    {'date': '2017-05-23', 'tobs': 71.0}
    {'date': '2017-05-24', 'tobs': 74.0}
    {'date': '2017-05-25', 'tobs': 74.0}
    {'date': '2017-05-26', 'tobs': 74.0}
    {'date': '2017-05-27', 'tobs': 74.0}
    {'date': '2017-05-28', 'tobs': 80.0}
    {'date': '2017-05-29', 'tobs': 74.0}
    {'date': '2017-05-30', 'tobs': 72.0}
    {'date': '2017-05-31', 'tobs': 75.0}
    {'date': '2017-06-01', 'tobs': 80.0}
    {'date': '2017-06-02', 'tobs': 76.0}
    {'date': '2017-06-03', 'tobs': 76.0}
    {'date': '2017-06-04', 'tobs': 77.0}
    {'date': '2017-06-05', 'tobs': 75.0}
    {'date': '2017-06-06', 'tobs': 75.0}
    {'date': '2017-06-07', 'tobs': 75.0}
    {'date': '2017-06-08', 'tobs': 75.0}
    {'date': '2017-06-09', 'tobs': 72.0}
    {'date': '2017-06-10', 'tobs': 74.0}
    {'date': '2017-06-11', 'tobs': 74.0}
    {'date': '2017-06-12', 'tobs': 74.0}
    {'date': '2017-06-13', 'tobs': 76.0}
    {'date': '2017-06-14', 'tobs': 74.0}
    {'date': '2017-06-15', 'tobs': 75.0}
    {'date': '2017-06-16', 'tobs': 73.0}
    {'date': '2017-06-17', 'tobs': 79.0}
    {'date': '2017-06-18', 'tobs': 75.0}
    {'date': '2017-06-19', 'tobs': 72.0}
    {'date': '2017-06-20', 'tobs': 72.0}
    {'date': '2017-06-21', 'tobs': 74.0}
    {'date': '2017-06-22', 'tobs': 72.0}
    {'date': '2017-06-23', 'tobs': 72.0}
    {'date': '2017-06-24', 'tobs': 77.0}
    {'date': '2017-06-25', 'tobs': 71.0}
    {'date': '2017-06-26', 'tobs': 73.0}
    {'date': '2017-06-27', 'tobs': 76.0}
    {'date': '2017-06-28', 'tobs': 77.0}
    {'date': '2017-06-29', 'tobs': 76.0}
    {'date': '2017-06-30', 'tobs': 76.0}
    {'date': '2017-07-01', 'tobs': 79.0}
    {'date': '2017-07-02', 'tobs': 81.0}
    {'date': '2017-07-03', 'tobs': 76.0}
    {'date': '2017-07-04', 'tobs': 78.0}
    {'date': '2017-07-05', 'tobs': 77.0}
    {'date': '2017-07-06', 'tobs': 74.0}
    {'date': '2017-07-07', 'tobs': 75.0}
    {'date': '2017-07-08', 'tobs': 78.0}
    {'date': '2017-07-09', 'tobs': 78.0}
    {'date': '2017-07-10', 'tobs': 69.0}
    {'date': '2017-07-11', 'tobs': 72.0}
    {'date': '2017-07-12', 'tobs': 74.0}
    {'date': '2017-07-13', 'tobs': 74.0}
    {'date': '2017-07-14', 'tobs': 76.0}
    {'date': '2017-07-15', 'tobs': 80.0}
    {'date': '2017-07-16', 'tobs': 80.0}
    {'date': '2017-07-17', 'tobs': 76.0}
    {'date': '2017-07-18', 'tobs': 76.0}
    {'date': '2017-07-19', 'tobs': 76.0}
    {'date': '2017-07-20', 'tobs': 77.0}
    {'date': '2017-07-21', 'tobs': 77.0}
    {'date': '2017-07-22', 'tobs': 77.0}
    {'date': '2017-07-23', 'tobs': 82.0}
    {'date': '2017-07-24', 'tobs': 75.0}
    {'date': '2017-07-25', 'tobs': 77.0}
    {'date': '2017-07-26', 'tobs': 75.0}
    {'date': '2017-07-27', 'tobs': 76.0}
    {'date': '2017-07-28', 'tobs': 81.0}
    {'date': '2017-07-29', 'tobs': 82.0}
    {'date': '2017-07-30', 'tobs': 81.0}
    {'date': '2017-07-31', 'tobs': 76.0}
    {'date': '2017-08-04', 'tobs': 77.0}
    {'date': '2017-08-05', 'tobs': 82.0}
    {'date': '2017-08-06', 'tobs': 83.0}
    {'date': '2017-08-13', 'tobs': 77.0}
    {'date': '2017-08-14', 'tobs': 77.0}
    {'date': '2017-08-15', 'tobs': 77.0}
    {'date': '2017-08-16', 'tobs': 76.0}
    {'date': '2017-08-17', 'tobs': 76.0}
    {'date': '2017-08-18', 'tobs': 79.0}
]

# Dictionary of Stations
stations_dict = [
    {'id': 1, 'station': 'USC00519397', 'name': 'WAIKIKI 717.2, HI US', 'latitude': 21.2716, 'longitude': -157.8168, 'elevation': 3.0}
    {'id': 2, 'station': 'USC00513117', 'name': 'KANEOHE 838.1, HI US', 'latitude': 21.4234, 'longitude': -157.8015, 'elevation': 14.6}
    {'id': 3, 'station': 'USC00514830', 'name': 'KUALOA RANCH HEADQUARTERS 886.9, HI US', 'latitude': 21.5213, 'longitude': -157.8374, 'elevation': 7.0}
    {'id': 4, 'station': 'USC00517948', 'name': 'PEARL CITY, HI US', 'latitude': 21.3934, 'longitude': -157.9751, 'elevation': 11.9}
    {'id': 5, 'station': 'USC00518838', 'name': 'UPPER WAHIAWA 874.3, HI US', 'latitude': 21.4992, 'longitude': -158.0111, 'elevation': 306.6}
    {'id': 6, 'station': 'USC00519523', 'name': 'WAIMANALO EXPERIMENTAL FARM, HI US', 'latitude': 21.33556, 'longitude': -157.71139, 'elevation': 19.5}
    {'id': 7, 'station': 'USC00519281', 'name': 'WAIHEE 837.5, HI US', 'latitude': 21.45167, 'longitude': -157.84888999999998, 'elevation': 32.9}
    {'id': 8, 'station': 'USC00511918', 'name': 'HONOLULU OBSERVATORY 702.2, HI US', 'latitude': 21.3152, 'longitude': -157.9992, 'elevation': 0.9}
    {'id': 9, 'station': 'USC00516128', 'name': 'MANOA LYON ARBO 785.2, HI US', 'latitude': 21.3331, 'longitude': -157.8025, 'elevation': 152.4}
]

# 2. Create an app, being sure to pass __name__
app = Flask(__name__)


# 3. Define what to do when a user hits the index route
@app.route("/")
def welcome():
    print("")
    return (
        f"Welcome to the Vacation API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"api/v1.0/stations"
        f"api/v1.0/tobs"
    )


# 4. Define what to do when a user hits the /about route
@app.route("/api/v1.0/precipitation")
def api/v1.0/precipitation():
    print("")
    return jsonify(busiest_station_prcp_dict)

@app.route("/api/v1.0/stations")
def /api/v1.0/stations():
    print("")
    return jsonify(stations_dict)

@app.route("/api/v1.0/tobs")
def /api/v1.0/stations():
    print("")
    return jsonify(busiest_station_tobs_dict)



@app.route("/api/v1.0/<start>")
def /api/v1.0/stations():
    print("Yess sir")
    return "Say hey"



@app.route("/api/v1.0/<start>/<end>")
def /api/v1.0/stations():
    print("Yess sir")
    return "Say hey"







if __name__ == "__main__":
    app.run(debug=True)
