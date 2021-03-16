import pandas as pd


class AlterDataframe:
    """
    Functions designed to make alterations to a Pandas dataframe
    df(Dataframe), dct(dictionary)
    """
    def __init__(self, df):
        self.df = df

    def fill_null_set_type(self, dct):
        """Fills null values and sets column types
            dct:{
                column_1: ["col_name", "str or int"],
                column_2: ["col_name", "str or int"],
             ...}"""
        for _, k in enumerate(dct):
            val = dct[k]
            if val == "str":
                self.df[k].fillna("Unknown", inplace=True)
                self.df[k] = self.df[k].astype(str)
            elif val == "int":
                self.df[k].fillna(0, inplace=True)
                self.df[k] = self.df[k].astype(int)
        return self.df

    def filter_out_rows(self, dct):
        """Filter out a rows with a specific value within designated columns
        dct:{"col_1": "val_1", "col_2": "val_2", ...}"""
        # new_df = self.df.copy()
        for col_name in dct:
            values_lst = dct[col_name]
            mask = -self.df[col_name].isin(values_lst)
            self.df = self.df[mask]
        # print(self.df)
        return self.df

    # def build_unique_df(self):
    #     """Builds an array of unique keys and values
    #     dct:{}"""
    #     for col in self.dct:
    #         gb_obj = self.df.groupby(self.dct[col])

    # def rename_columns(self):
    #     pass


# cols = ["Name", "Position", "Status"]
# data = [["Erza", "Leader", "Active"], ["Atlas", "Knight", "In-Active"], ["Sepra", "Spy", "Active"]]
# df = pd.DataFrame(data, columns=cols)
# dct = {"Position": ["Spy"], "Status": ["In-Active"]}
# obj_df = AlterDataframe(df, dct)
# df = obj_df.filter_out_rows()
