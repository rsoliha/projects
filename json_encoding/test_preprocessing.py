import unittest
import json_encoding.preprocessing as preprocessing

class TestPreprocessing(unittest.TestCase):

  def test_remove_dots(self):
    result=preprocessing.remove_dots("...")
    self.assertEqual(result,"...")
    result=preprocessing.remove_dots(".T.h.is")
    self.assertEqual(result,".T.h.is")

  def test_remove_escape_chars(self):
    result=preprocessing.remove_escape_chars("\"\"")
    self.assertEqual(result,"")
    result=preprocessing.remove_escape_chars("\"This text is using \"quotes\".\"")
    self.assertEqual(result,"This text is using \"quotes\".")

  def test_cleaning(self):
    test_dict = {"properties":{"name1":"\".H.E.I.Z.G.R.U.P.P.E\"",
                               "name2":"\".T.E.M.P.E.R.A.T.U.R.E...1.F...2.2.5\"",
                               "name3":".H.E.I.Z.G.R.U.P.P.E",
                               "name4":"H.E.I.Z.G.R.U.P.P.E.",
                               "name5":"\"This text is using \"quotes\".\"",
                               "name6":"T.h.i.s. is a special test case",
                               "name7":"................",
                               "name8":"",
                               "name9":"\"\""}}
    predicted_dict = {"properties":{"name1":"HEIZGRUPPE",
                               "name2":"TEMPERATURE.1F.225",
                               "name3":"HEIZGRUPPE",
                               "name4":"HEIZGRUPPE",
                               "name5":"This text is using \"quotes\".",
                               "name6":"T.h.i.s. is a special test case",
                               "name7":"........",
                               "name8":"",
                               "name9":""}}
    result=preprocessing.cleaning(test_dict)
    self.assertDictEqual(result,predicted_dict)


if __name__ == '__main__':
  unittest.main()
