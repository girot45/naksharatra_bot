# -*- coding: utf-8 -*-

from datetime import datetime

import matplotlib as mpl
import numpy as np
import pytz
from astropy.coordinates import get_body, EarthLocation
from astropy.table import Table
from astropy.time import Time
from matplotlib import pyplot as plt
from timezonefinder import TimezoneFinder



from naksharatra.calc_rahu_ketu_pos import \
    calc_rahu_ketu_pos
from naksharatra.plot_graha import \
    plot_outer_graha, plot_inner_graha_phase, plot_rahu, plot_ketu, \
    plot_sun, plot_moon_phase
from settings import nakshatra_settings, plot_settings, astro_objects

from naksharatra.util import calc_nakshatram_coords

from settings.nakshatra_settings.schemas import AstroObjectName

##########################################



mpl.use("pgf")

## TeX preamble ##


params = {
    'font.family': 'sans-serif',
    'font.sans-serif': 'Arial',
    'text.usetex': True,
    'pgf.rcfonts': False,
    'pgf.texsystem': 'xelatex',
    'pgf.preamble': plot_settings.preamble,
}

mpl.rcParams.update(params)

plt.style.use('dark_background')


##########################################

def calc_nakshatra_tithi(
        location, time, time_format="%Y-%m-%d %H:%M:%S",
        fs: float=11.5,
        filename="res_img/res.png"
        ):
    """
    Calculates nakshatra and tithi at input time and makes plot of grahas

    Inputs :
    location = enter address of your location. Eg: "Mumbai, India"
    time = time at which to calculate panchanga
    time_format = format of input time
    filename = name of file to write the plot of position of grahas in nakshatra and rashi

    Output :
    Plot saved at filename
    """
    plt.rcParams.update({'font.size': fs})

    nakshatram_coords = calc_nakshatram_coords()

    for i in range(len(nakshatram_coords)):
        if nakshatram_coords[i] > nakshatra_settings.full_circle_degs:
            nakshatram_coords[i] = nakshatram_coords[i] - 360

    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'},
                           figsize=(7, 5))

    ax.set_rmax(2.5)
    ax.set_yticks([1])
    ax.set_yticklabels([""])
    ax.grid(axis="x")

    observing_location = EarthLocation.of_address(location)
    tz_obj = TimezoneFinder()
    timezone_location = tz_obj.timezone_at(
        lng=observing_location.lon.value,
        lat=observing_location.lat.value)

    fmt = time_format
    date_str = time

    tz = pytz.timezone(timezone_location)
    test_date = datetime.strptime(date_str, fmt)
    day_of_the_week_at_t = test_date.strftime('%A')
    local_time = tz.localize(test_date, is_dst=None)
    test_date_utc = local_time.astimezone(pytz.utc)

    test_date_utc_time = Time(test_date_utc.strftime(fmt),
                              format="iso", scale="utc")

    moon_coord = get_body(AstroObjectName.moon, test_date_utc_time)
    sun_coord = get_body(AstroObjectName.sun, test_date_utc_time)

    moon_lambda = moon_coord.geocentrictrueecliptic.lon.value
    sun_lambda = sun_coord.geocentrictrueecliptic.lon.value

    d_theta = moon_lambda - sun_lambda

    if sun_lambda > moon_lambda:
        d_theta += 360


    final_tithi = d_theta / nakshatra_settings.each_tithi
    final_nakshatram = ""

    # внешние радиальные линиии

    for coord_id, coord in enumerate(nakshatram_coords):
        ax.plot(
            np.deg2rad([coord, coord]),
            [1, 2.2],
            plot_settings.outer_radial_lines_colour,
            alpha=plot_settings.lines_transparency,
        )
        if coord > nakshatra_settings.full_circle_degs:
            nakshatram_coords[coord_id] = coord - nakshatra_settings.full_circle_degs
        text_theta = (
            (2 * nakshatram_coords[coord_id] + nakshatra_settings.nakshatram_extent) *
            (np.pi / nakshatra_settings.full_circle_degs)
        )
        if 90 < coord < 270:
            if coord < moon_lambda < coord + nakshatra_settings.nakshatram_extent:
                ax.text(text_theta, 1.5, nakshatra_settings.nakshatram_names[coord_id],
                        rotation=text_theta * 180 / np.pi + 180,
                        ha="center", va="center", color="#fff")
                final_nakshatram = nakshatra_settings.nakshatram_names[coord_id]
            else:
                ax.text(text_theta, 1.5, nakshatra_settings.nakshatram_names[coord_id],
                        rotation=text_theta * 180 / np.pi + 180,
                        ha="center", va="center", alpha=0.45, color="#fff")
        else:
            if coord < moon_lambda < coord + nakshatra_settings.nakshatram_extent:
                ax.text(text_theta, 1.5, nakshatra_settings.nakshatram_names[coord_id],
                        rotation=text_theta * 180 / np.pi,
                        ha="center", va="center", color="#fff")
                final_nakshatram = nakshatra_settings.nakshatram_names[coord_id]
            elif ((moon_lambda + 360 - coord) < nakshatra_settings.nakshatram_extent):
                ax.text(text_theta, 1.5, nakshatra_settings.nakshatram_names[coord_id],
                        rotation=text_theta * 180 / np.pi,
                        ha="center", va="center", color="#fff")
                final_nakshatram = nakshatra_settings.nakshatram_names[coord_id]
            else:
                ax.text(text_theta, 1.5, nakshatra_settings.nakshatram_names[coord_id],
                        rotation=text_theta * 180 / np.pi,
                        ha="center", va="center", alpha=0.45, color="#fff")
    ax.set_xticks(np.pi / 180 * nakshatram_coords)
    ax.set_xticklabels([])

    plot_moon_phase(final_tithi,
                    np.array([np.pi / 180 * moon_lambda, 1]), 0.1,
                    fig, ax)
    plot_sun(np.array([np.pi / 180 * sun_lambda, 2.05]), 0.1, fig, ax)

    #####################################



    rashi_coords = np.linspace(nakshatra_settings.rashi_start,
                               nakshatra_settings.rashi_start + nakshatra_settings.rashi_extent * 11, 12)
    # внутренние радиальные линии
    for coord_id, coord in enumerate(rashi_coords):
        ax.plot(np.deg2rad([coord, coord]), [0, 1], "#fff", alpha=0.3)
        rashi_text_theta = (2 * rashi_coords[
            coord_id] + nakshatra_settings.rashi_extent) * (np.pi / 360)
        if (77 < coord < 255):
            if (coord < sun_lambda < coord + nakshatra_settings.rashi_extent):
                ax.text(rashi_text_theta, 0.625,
                        nakshatra_settings.rashi_names[coord_id],
                        rotation=rashi_text_theta * 180 / np.pi + 180,
                        ha="center", va="center", color="#fff")
            else:
                ax.text(rashi_text_theta, 0.625,
                        nakshatra_settings.rashi_names[coord_id],
                        rotation=rashi_text_theta * 180 / np.pi + 180,
                        ha="center", va="center", alpha=0.45, color="#fff")
        else:
            if (coord < sun_lambda < coord + nakshatra_settings.rashi_extent):
                ax.text(rashi_text_theta, 0.625,
                        nakshatra_settings.rashi_names[coord_id],
                        rotation=rashi_text_theta * 180 / np.pi,
                        ha="center", va="center", color="#fff")
            elif ((sun_lambda + 360 - coord) < nakshatra_settings.rashi_extent):
                ax.text(rashi_text_theta, 0.625,
                        nakshatra_settings.rashi_names[coord_id],
                        rotation=rashi_text_theta * 180 / np.pi,
                        ha="center", va="center", color="#fff")
            else:
                ax.text(rashi_text_theta, 0.625,
                        nakshatra_settings.rashi_names[coord_id],
                        rotation=rashi_text_theta * 180 / np.pi,
                        ha="center", va="center", alpha=0.45, color="#fff")

    ################ plot other grahas #####################

    ### Inner grahas ###

    mercury_lambda = get_body("mercury",
                              test_date_utc_time).geocentrictrueecliptic.lon.value
    venus_lambda = get_body("venus",
                            test_date_utc_time).geocentrictrueecliptic.lon.value


    plot_inner_graha_phase("mercuri",
                           [np.deg2rad(mercury_lambda), 1.9], 0.05,
                           ax)
    plot_inner_graha_phase("venus",
                           [np.deg2rad(venus_lambda), 1.9], 0.05,
                           ax)

    ### Outer grahas ###

    mars_lambda = get_body("mars",
                           test_date_utc_time).geocentrictrueecliptic.lon.value
    jupiter_lambda = get_body("jupiter",
                              test_date_utc_time).geocentrictrueecliptic.lon.value
    saturn_lambda = get_body("saturn",
                             test_date_utc_time).geocentrictrueecliptic.lon.value

    plot_outer_graha("mars", [np.deg2rad(mars_lambda), 1.9], 0.05,
                     fig, ax)
    plot_outer_graha("jupiter", [np.deg2rad(jupiter_lambda), 1.9], 0.05,
                     fig, ax)
    plot_outer_graha("saturn", [np.deg2rad(saturn_lambda), 1.9], 0.05,
                     fig, ax)

    ##  rahu and ketu  ##


    moon_lambda_known_eclipse = get_body("moon",
                                         nakshatra_settings.known_eclipse_time).geocentrictrueecliptic.lon.value
    rahu_lambda, ketu_lambda = calc_rahu_ketu_pos(
        test_date_utc_time,
        moon_lambda_known_eclipse
    )

    rahu_lambda, ketu_lambda = ketu_lambda, rahu_lambda

    plot_rahu([np.deg2rad(rahu_lambda), 1.9], 5, fig, ax)
    plot_ketu([np.deg2rad(ketu_lambda), 1.9], 5, fig, ax)

    ################ legend for grahas #####################

    inv = ax.transData.inverted()

    sun_legend_pos = inv.transform((750, 450))
    sun_label_pos = inv.transform((790, 445))
    moon_legend_pos = inv.transform((750, 400))
    moon_label_pos = inv.transform((790, 395))
    mercury_legend_pos = inv.transform((750, 350))
    mercury_label_pos = inv.transform((790, 345))
    venus_legend_pos = inv.transform((750, 300))
    venus_label_pos = inv.transform((790, 295))
    mars_legend_pos = inv.transform((750, 250))
    mars_label_pos = inv.transform((790, 245))
    jupiter_legend_pos = inv.transform((750, 200))
    jupiter_label_pos = inv.transform((790, 195))
    saturn_legend_pos = inv.transform((750, 150))
    saturn_label_pos = inv.transform((790, 145))
    rahu_legend_pos = inv.transform((750, 100))
    rahu_label_pos = inv.transform((790, 95))
    ketu_legend_pos = inv.transform((750, 50))
    ketu_label_pos = inv.transform((790, 45))

    plot_sun(sun_legend_pos, 0.1, fig, ax)
    plt.text(sun_label_pos[0], sun_label_pos[1], "\sam{Солнце} ")
    plot_moon_phase(final_tithi, moon_legend_pos, 0.1, fig, ax)
    plt.text(moon_label_pos[0], moon_label_pos[1], "\sam{Луна} ")
    plot_inner_graha_phase("mercuri",
                           mercury_legend_pos, 0.05, ax)
    plt.text(mercury_label_pos[0], mercury_label_pos[1],
             "\sam{Меркурий} ")
    plot_inner_graha_phase("venus",
                           venus_legend_pos, 0.05, ax)
    plt.text(venus_label_pos[0], venus_label_pos[1], "\sam{Венера} ")
    plot_outer_graha("mars", mars_legend_pos, 0.05, fig, ax)
    plt.text(mars_label_pos[0], mars_label_pos[1], "\sam{Марс} ")
    plot_outer_graha("jupiter", jupiter_legend_pos, 0.05, fig, ax)
    plt.text(jupiter_label_pos[0], jupiter_label_pos[1],
             "\sam{Юпитер} ")
    plot_outer_graha("saturn", saturn_legend_pos, 0.05, fig, ax)
    plt.text(saturn_label_pos[0], saturn_label_pos[1],
             "\sam{Сатурн} ")

    plot_rahu(rahu_legend_pos, 5, fig, ax)
    plt.text(rahu_label_pos[0], rahu_label_pos[1], "\sam{Раху} ")
    plot_ketu(ketu_legend_pos, 5, fig, ax)
    plt.text(ketu_label_pos[0], ketu_label_pos[1], "\sam{Кету} ")

    ################ legend for panchanga #####################

    plt.text(inv.transform((-200, 500))[0],
             inv.transform((-200, 500))[1], location)
    plt.text(inv.transform((-195, 470))[0],
             inv.transform((-195, 470))[1], date_str.split(" ")[0])
    plt.text(inv.transform((-190, 440))[0],
             inv.transform((-190, 440))[1], date_str.split(" ")[1])

    plt.text(inv.transform((-170, 340))[0],
             inv.transform((-170, 340))[1], "\sam{День рождения}",
             bbox=dict(facecolor='none', edgecolor='white'))
    tithi_names_file = nakshatra_settings.tithi_filename
    tithi_names_tab = Table.read(tithi_names_file, format="latex")
    tithi_number = tithi_names_tab['tithi'].data
    tithi_names = tithi_names_tab['tithi_names'].data

    plt.text(inv.transform((-170, 310))[0],
             inv.transform((-170, 310))[1],
             tithi_names[int(final_tithi)], fontsize=fs)
    vaar_names_file = nakshatra_settings.vaara_filename

    vaara_names_tab = Table.read(vaar_names_file, format="latex")
    weekday = vaara_names_tab['weekday'].data
    vaara_names = vaara_names_tab['vaara'].data

    plt.text(inv.transform((-170, 280))[0],
             inv.transform((-170, 280))[1],
             vaara_names[np.where(weekday == day_of_the_week_at_t)][0],
             fontsize=fs)

    plt.text(inv.transform((-170, 250))[0],
             inv.transform((-170, 250))[1], final_nakshatram, fontsize=fs)

    # plt.title(r'\sam{Ом}', fontsize=20 , y=1.07)
    plt.ylim(0, 2.15)
    fig.set_size_inches(13, 10)

    plt.savefig(filename)
    plt.close()

    return 0


