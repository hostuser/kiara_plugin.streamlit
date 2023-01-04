# -*- coding: utf-8 -*-
from kiara import Value
from kiara_plugin.tabular.models.array import KiaraArray
from kiara_plugin.tabular.models.db import KiaraDatabase
from kiara_plugin.tabular.models.table import KiaraTable
from streamlit.delta_generator import DeltaGenerator

from kiara_plugin.streamlit.components.preview import PreviewComponent


class ArrayPreview(PreviewComponent):

    _component_name = "array_preview"

    @classmethod
    def get_data_type(cls) -> str:
        return "array"

    def render_preview(self, st: DeltaGenerator, key: str, value: Value):

        table: KiaraArray = value.data

        st.dataframe(table.to_pandas(), use_container_width=True)


class TablePreview(PreviewComponent):

    _component_name = "table_preview"

    @classmethod
    def get_data_type(cls) -> str:
        return "table"

    def render_preview(self, st: DeltaGenerator, key: str, value: Value):

        table: KiaraTable = value.data

        st.dataframe(table.to_pandas(), use_container_width=True)


class DatabasePreview(PreviewComponent):

    _component_name = "database_preview"

    @classmethod
    def get_data_type(cls) -> str:
        return "database"

    def render_preview(self, st: DeltaGenerator, key: str, value: Value):

        db: KiaraDatabase = value.data
        tabs = st.tabs(db.table_names)

        for idx, table_name in enumerate(db.table_names):
            # TODO: this is probably not ideal, as it always loads all tables because
            # of how tabs are implemented in streamlit
            # maybe there is an easy way to do this better, otherwise, maybe not use tabs
            table = db.get_table_as_pandas_df(table_name)
            tabs[idx].dataframe(table, use_container_width=True)


class DatabasePreview(PreviewComponent):

    _component_name = "network_data_preview"

    @classmethod
    def get_data_type(cls) -> str:
        return "network_data"

    def render_preview(self, st: DeltaGenerator, key: str, value: Value):

        db: KiaraDatabase = value.data
        tabs = st.tabs(db.table_names)

        for idx, table_name in enumerate(db.table_names):
            # TODO: this is probably not ideal, as it always loads all tables because
            # of how tabs are implemented in streamlit
            # maybe there is an easy way to do this better, otherwise, maybe not use tabs
            table = db.get_table_as_pandas_df(table_name)
            tabs[idx].dataframe(table, use_container_width=True)
