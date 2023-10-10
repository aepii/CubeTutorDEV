import requests
import json
from bs4 import BeautifulSoup

def get_data(algorithm_sets):
    all_algorithms = {}

    for algorithm_set in algorithm_sets:

        all_algorithms[algorithm_set] = {}

        url = "https://www.speedcubedb.com/a/3x3/" + algorithm_set
        res = requests.get(url)
        soup = BeautifulSoup(res.content, 'html.parser')

        datas = soup.select('div.singlealgorithm')

        for index, data in enumerate(datas):

            case_algorithms = []

            case = data.find('h3').text
            sub_group = data.get('data-subgroup')

            group_algorithms = data.find_all('li', attrs={'class': 'list-group-item'})

            for algorithm in group_algorithms:
                case_algorithms.append(algorithm.find("div").text)

            all_algorithms[algorithm_set][case] = case_algorithms

    algorithms_json = json.dumps(all_algorithms, indent=4)
    print(algorithms_json)


def main():
    get_data(["PLL", "OLL"])


if __name__ == "__main__":
    main()
