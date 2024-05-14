# -*- coding: utf-8 -*-
from astropy import units as u
from settings import nakshatra_settings


def calc_time_difference(known_eclipse_time, test_date_utc_time):
    if test_date_utc_time.jd > known_eclipse_time.jd:
        return  ((test_date_utc_time - known_eclipse_time).value * u.d).to(u.year)
    else:
        return ((known_eclipse_time - test_date_utc_time).value * u.d).to(u.year)


def calc_ketu_lambda(
        test_date_utc_time,
        moon_lambda_known_eclipse,
        known_eclipse_time = nakshatra_settings.known_eclipse_time,
):
    time_diff = calc_time_difference(known_eclipse_time, test_date_utc_time)
    ketu_degrees_moved = ((nakshatra_settings.ketu_speed * time_diff.value) %
                           nakshatra_settings.full_circle_degs)
    if test_date_utc_time.jd <= known_eclipse_time.jd:
        ketu_lambda = moon_lambda_known_eclipse - ketu_degrees_moved
        if ketu_lambda < 0:
            ketu_lambda = nakshatra_settings.full_circle_degs - ketu_lambda
    else:
        ketu_lambda = moon_lambda_known_eclipse + ketu_degrees_moved
        if ketu_degrees_moved > nakshatra_settings.full_circle_degs:
            ketu_lambda = nakshatra_settings.full_circle_degs - ketu_lambda
    return ketu_lambda


def calc_rahu_lambda(ketu_lambda):
    if ketu_lambda < nakshatra_settings.full_circle_degs // 2:
        return nakshatra_settings.full_circle_degs // 2 + ketu_lambda
    else:
        return ((nakshatra_settings.full_circle_degs // 2 + ketu_lambda) -
                nakshatra_settings.full_circle_degs)


def calc_rahu_ketu_pos(
        test_date_utc_time,
        moon_lambda_known_eclipse
):
    ketu_lambda = calc_ketu_lambda(
        test_date_utc_time,
        moon_lambda_known_eclipse
    )
    rahu_lambda = calc_rahu_lambda(ketu_lambda)
    return rahu_lambda, ketu_lambda
