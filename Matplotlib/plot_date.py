import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime
from thesis_format import ThesisFormat


class DateFormat(ThesisFormat):
    def __init__(self) -> None:
        super().__init__()
    
    def data_stockprices(self):
        # 2021年1月から2021年6月までの1週間ごとの日付データを作成
        start_date = datetime.datetime(2021, 1, 1)
        end_date = datetime.datetime(2021, 3, 30)
        # 日付の空リストを作成
        date_list = []
        current_date = start_date
        while current_date <= end_date:
            # 日付の空リストに日付を追加
            date_list.append(current_date)
            # 1週間後の日付に更新
            current_date += datetime.timedelta(weeks=1)

        # 3社の株価リストを作成（date_listと同じ要素数）
        company1_stock_prices = [100, 105, 102, 110, 108, 115, 120, 118, 122, 125, 130, 128, 135]
        company2_stock_prices = [80, 85, 88, 90, 92, 95, 100, 98, 102, 105, 110, 108, 105]
        company3_stock_prices = [120, 125, 130, 135, 138, 140, 142, 145, 148, 150, 152, 155, 158]

        return date_list, company1_stock_prices, company2_stock_prices, company3_stock_prices

    def plt_simple(self):
        # step1 データ作成関数を呼び出し
        date_list, company1_stock_prices, company2_stock_prices, company3_stock_prices = self.data_stockprices()

        # step2 グラフフレームの作成
        fig, ax = plt.subplots()
        # step3 時系列グラフの描画
        ax.plot_date(date_list, company1_stock_prices, label='Company 1')
        ax.plot_date(date_list, company2_stock_prices, label='Company 2')
        ax.plot_date(date_list, company3_stock_prices, label='Company 3')

        #step4 軸のカスタム
        ax.set_xlabel('Time label')
        ax.set_ylabel('Y label')  
        ax.legend()
        ax.set_title('Chart with time axis')

        plt.show()

    def plt_fmt(self):
        # step1 データ作成関数を呼び出し
        date_list, company1_stock_prices, company2_stock_prices, company3_stock_prices = self.data_stockprices()

        # step2 グラフフレームの作成
        fig, ax = plt.subplots()
        # step3 時系列グラフの描画
        ax.plot_date(date_list, company1_stock_prices, 'og--', label='Company 1')
        ax.plot_date(date_list, company2_stock_prices, 'sr-.', label='Company 2')
        ax.plot_date(date_list, company3_stock_prices, '*c:', label='Company 3')

        #step4 軸のカスタム
        ax.set_xlabel('Time label')
        ax.set_ylabel('Y label')  
        ax.legend()
        ax.set_title('Chart with time axis')

        plt.show()

    def plt_timezone(self):
        # step1 データ作成関数を呼び出し
        date_list, company1_stock_prices, company2_stock_prices, company3_stock_prices = self.data_stockprices()

        # step2 グラフフレームの作成
        fig, ax = plt.subplots()
        # step3 時系列グラフの描画
        ax.plot_date(date_list, company1_stock_prices, 'o-', tz='JST', label='Company 1')
        ax.plot_date(date_list, company2_stock_prices, 'o-', tz='JST', label='Company 2')
        ax.plot_date(date_list, company3_stock_prices, 'o-', tz='JST', label='Company 3')

        #step4 軸のカスタム
        ax.set_xlabel('Time label')
        ax.set_ylabel('Y label')  
        ax.legend()
        ax.set_title('Chart with time axis')

        plt.show()

    def plt_ydate(self):
        # step1 データ作成関数を呼び出し
        date_list, company1_stock_prices, company2_stock_prices, company3_stock_prices = self.data_stockprices()

        # step2 グラフフレームの作成
        fig, ax = plt.subplots()
        # step3 時系列グラフの描画
        ax.plot_date(company1_stock_prices, date_list, 'o-', xdate=False, ydate=True, label='Company 1')
        ax.plot_date(company2_stock_prices, date_list, 'o-', xdate=False, ydate=True, label='Company 2')
        ax.plot_date(company3_stock_prices, date_list, 'o-', xdate=False, ydate=True, label='Company 3')

        #step4 軸のカスタム
        ax.set_xlabel('Time label')
        ax.set_ylabel('Y label')  
        ax.legend()
        ax.set_title('Chart with time axis')

        plt.show()
    
    def plt_locater(self):
        # step1 データ作成関数を呼び出し
        date_list, company1_stock_prices, company2_stock_prices, company3_stock_prices = self.data_stockprices()

        # step2 グラフフレームの作成
        fig, ax = plt.subplots()

        # step3 時系列グラフの描画
        ax.plot_date(date_list, company1_stock_prices, 'o-', label='Company 1')
        ax.plot_date(date_list, company2_stock_prices, 'o-', label='Company 2')
        ax.plot_date(date_list, company3_stock_prices, 'o-', label='Company 3')

        #step4 軸のカスタム
        locator = mdates.AutoDateLocator(maxticks=15)
        ax.xaxis.set_major_locator(locator)

        ax.set_xlabel('Time label')
        ax.set_ylabel('Y label')  
        ax.legend()
        ax.set_title('Chart with time axis (AutoDateLocator)')

        plt.show()

    def plt_format(self):
        # step1 データ作成関数を呼び出し
        date_list, company1_stock_prices, company2_stock_prices, company3_stock_prices = self.data_stockprices()

        # step2 グラフフレームの作成
        fig, ax = plt.subplots()

        # step3 時系列グラフの描画
        ax.plot_date(date_list, company1_stock_prices, 'o-', label='Company 1')
        ax.plot_date(date_list, company2_stock_prices, 'o-', label='Company 2')
        ax.plot_date(date_list, company3_stock_prices, 'o-', label='Company 3')

        #step4 軸のカスタム
        locator = mdates.AutoDateLocator(maxticks=15)
        ax.xaxis.set_major_locator(locator)
        # 変更 '%b'→'%Y-%b'
        # formats=['%Y', '%Y-%b', '%d', '%H:%M', '%H:%M', '%S.%f']
        # 変更 '%Y-%b'→'%Y'
        offset_formats=['', '%Y', '%Y', '%Y-%b-%d', '%Y-%b-%d', '%Y-%b-%d %H:%M']
        formatter = mdates.ConciseDateFormatter(locator, offset_formats=offset_formats, usetex=True)
        ax.xaxis.set_major_formatter(formatter)

        ax.set_xlabel('Time label')
        ax.set_ylabel('Y label')  
        ax.legend()
        ax.set_title('Chart with time axis (ConciseDateFormatter)')

        plt.show()

if __name__ == '__main__':
    date_plt = DateFormat()
    # date_plt.plt_simple()
    # date_plt.plt_fmt()
    # date_plt.plt_timezone()
    # date_plt.plt_ydate()
    # date_plt.plt_locater()
    date_plt.plt_format()