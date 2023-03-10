from collections import OrderedDict
import pandas as pd
from tests import project_test, assert_output, generate_random_tickers


@project_test
def test_days_to_weeks(fn):
    tickers = generate_random_tickers(3)
    dates = pd.date_range('10/10/2018', periods=28, freq='D')
    resampled_dates = [
        pd.Timestamp('2018-10-14 00:00:00', freq='W-SUN'),
        pd.Timestamp('2018-10-21 00:00:00', freq='W-SUN'),
        pd.Timestamp('2018-10-28 00:00:00', freq='W-SUN'),
        pd.Timestamp('2018-11-04 00:00:00', freq='W-SUN'),
        pd.Timestamp('2018-11-11 00:00:00', freq='W-SUN')]

    fn_inputs = {
        'open_prices': pd.DataFrame(
            [
                [24, 21, 43],
                [14, 22, 41],
                [29, 23, 44],
                [44, 14, 13],
                [31, 28, 34],
                [36, 49, 27],
                [48, 20, 46],
                [48, 37, 27],
                [16, 42, 22],
                [23, 36, 32],
                [13, 31, 28],
                [23, 33, 18],
                [14, 47, 45],
                [28, 21, 31],
                [31, 36, 40],
                [19, 25, 46],
                [30, 46, 48],
                [19, 34, 35],
                [24, 13, 24],
                [48, 15, 39],
                [16, 34, 14],
                [37, 30, 28],
                [34, 24, 20],
                [17, 15, 38],
                [44, 15, 22],
                [24, 36, 28],
                [12, 41, 49],
                [24, 27, 14]],
            dates, tickers),
        'high_prices': pd.DataFrame(
            [
                [48, 48, 43],
                [42, 49, 47],
                [45, 47, 48],
                [48, 46, 48],
                [49, 49, 46],
                [40, 49, 49],
                [49, 44, 49],
                [49, 46, 48],
                [46, 49, 49],
                [49, 47, 47],
                [45, 49, 46],
                [45, 49, 49],
                [49, 48, 48],
                [48, 49, 49],
                [49, 49, 48],
                [48, 48, 49],
                [48, 47, 48],
                [47, 49, 49],
                [47, 49, 49],
                [48, 49, 48],
                [49, 49, 47],
                [48, 47, 48],
                [47, 48, 47],
                [49, 49, 45],
                [49, 49, 49],
                [47, 46, 48],
                [47, 47, 49],
                [49, 49, 46]],
            dates, tickers),
        'low_prices': pd.DataFrame(
            [
                [12, 12, 13],
                [12, 14, 15],
                [13, 14, 12],
                [14, 14, 13],
                [12, 12, 14],
                [12, 12, 12],
                [12, 12, 12],
                [13, 12, 13],
                [12, 12, 13],
                [14, 12, 14],
                [12, 12, 12],
                [13, 14, 16],
                [14, 13, 13],
                [13, 14, 12],
                [14, 12, 14],
                [15, 12, 13],
                [12, 12, 12],
                [12, 13, 15],
                [14, 12, 12],
                [12, 12, 12],
                [12, 14, 13],
                [12, 12, 13],
                [13, 14, 15],
                [12, 12, 12],
                [12, 14, 12],
                [12, 12, 13],
                [12, 12, 12],
                [16, 12, 14]],
            dates, tickers),
        'close_prices': pd.DataFrame(
            [
                [27, 45, 15],
                [40, 49, 40],
                [25, 26, 36],
                [26, 36, 19],
                [25, 34, 46],
                [22, 39, 45],
                [40, 14, 17],
                [42, 46, 33],
                [35, 41, 49],
                [14, 24, 31],
                [41, 18, 13],
                [36, 27, 18],
                [16, 16, 45],
                [37, 24, 16],
                [43, 40, 28],
                [39, 29, 45],
                [38, 20, 43],
                [44, 13, 34],
                [23, 17, 47],
                [25, 14, 38],
                [48, 44, 23],
                [37, 24, 33],
                [40, 28, 17],
                [31, 12, 44],
                [29, 40, 49],
                [18, 30, 13],
                [27, 16, 47],
                [31, 32, 14]],
            dates, tickers)}
    fn_correct_outputs = OrderedDict([
        (
            'open_prices_weekly',
            pd.DataFrame(
                [
                    [24, 21, 43],
                    [36, 49, 27],
                    [14, 47, 45],
                    [48, 15, 39],
                    [12, 41, 49]],
                resampled_dates, tickers)),
        (
            'high_prices_weekly',
            pd.DataFrame(
                [
                    [49, 49, 48],
                    [49, 49, 49],
                    [49, 49, 49],
                    [49, 49, 49],
                    [49, 49, 49]],
                resampled_dates, tickers)),
        (
            'low_prices_weekly',
            pd.DataFrame(
                [
                    [12, 12, 12],
                    [12, 12, 12],
                    [12, 12, 12],
                    [12, 12, 12],
                    [12, 12, 12]],
                resampled_dates, tickers)),
        (
            'close_prices_weekly',
            pd.DataFrame(
                [
                    [25, 34, 46],
                    [36, 27, 18],
                    [23, 17, 47],
                    [18, 30, 13],
                    [31, 32, 14]],
                resampled_dates, tickers))])

    assert_output(fn, fn_inputs, fn_correct_outputs)

    
@project_test
def test_calculate_returns(fn):
    tickers = generate_random_tickers(5)
    dates = generate_random_dates(6)

    fn_inputs = {
        'close': pd.DataFrame(
            [
                [21.050810483942833, 17.013843810658827, 10.984503755486879, 11.248093428369392, 12.961712733997235],
                [15.63570258751384, 14.69054309070934, 11.353027688995159, 475.74195118202061, 11.959640427803022],
                [482.34539247360806, 35.202580592515041, 3516.5416782257166, 66.405314327318209, 13.503960481087077],
                [10.918933017418304, 17.9086438675435, 24.801265417692324, 12.488954191854916, 10.52435923388642],
                [10.675971965144655, 12.749401436636365, 11.805257579935713, 21.539039489843024, 19.99766036804861],
                [11.545495378369814, 23.981468434099405, 24.974763062186504, 36.031962102997689, 14.304332320024963]],
            dates, tickers)}
    fn_correct_outputs = OrderedDict([
        (
            'returns',
            pd.DataFrame(
                [
                    [np.nan, np.nan, np.nan, np.nan, np.nan],
                    [-0.25723988, -0.13655355, 0.03354944, 41.29534136, -0.07731018],
                    [29.84897463, 1.39627496, 308.74483411, -0.86041737, 0.12912763],
                    [-0.97736283, -0.49126900, -0.99294726, -0.81192839, -0.22064647],
                    [-0.02225135, -0.28808672, -0.52400584, 0.72464717, 0.90013092],
                    [0.08144677, 0.88098779, 1.11556274, 0.67286764, -0.28469971]],
                dates, tickers))])

    assert_output(fn, fn_inputs, fn_correct_outputs)    