import json_encoding.utils as utils
import json_encoding.config as config
import json_encoding.preprocessing as preprocessing


def main():
  data = utils.load_json(config.file_path)
  data = preprocessing.start_cleaning(data)
  utils.save_json(config.file_save_path, data)


if __name__ == '__main__':
    main()
