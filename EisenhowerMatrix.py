import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode, DataReturnMode

# タイトル
st.title("アイゼンハワーのマトリクス（重要度-緊急度マトリクス）")

# 説明
st.write("""
このアプリを使って、タスクの優先順位を決定しましょう。
タスクを直接マトリクスに入力・編集し、アイゼンハワーのマトリクスに自動的に分類しましょう。
""")

# タスクを保存するデータフレームをセッションステートで保持
if "tasks" not in st.session_state:
    st.session_state["tasks"] = pd.DataFrame(columns=["タスク", "重要度", "緊急度"])

# AgGridを使ってデータフレームを編集可能に設定
def editable_grid(df):
    gb = GridOptionsBuilder.from_dataframe(df)
    gb.configure_pagination(paginationAutoPageSize=True)
    gb.configure_default_column(editable=True, groupable=True)
    gb.configure_selection(selection_mode="multiple", use_checkbox=True)
    gb.configure_grid_options(domLayout="normal")
    gridOptions = gb.build()

    grid_response = AgGrid(
        df,
        gridOptions=gridOptions,
        update_mode=GridUpdateMode.MODEL_CHANGED,
        data_return_mode=DataReturnMode.FILTERED_AND_SORTED,
        fit_columns_on_grid_load=True,
        enable_enterprise_modules=False,
        height=300,
        reload_data=True,
    )
    return grid_response

# タスクの編集用データフレーム
task_df = st.session_state["tasks"]
grid_response = editable_grid(task_df)

# データフレームの更新
st.session_state["tasks"] = grid_response["data"]

# アイゼンハワーのマトリクス表示
st.header("アイゼンハワーのマトリクス")
col1, col2 = st.columns([1, 1], gap="medium")
col3, col4 = st.columns([1, 1], gap="medium")

high_high = st.session_state["tasks"][(st.session_state["tasks"]["重要度"] == "高") & (st.session_state["tasks"]["緊急度"] == "高")]



with col1:
    st.subheader("緊急度：高、重要度：高（今すぐ実行）")
    high_high = st.session_state["tasks"][(st.session_state["tasks"]["重要度"] == "高") & (st.session_state["tasks"]["緊急度"] == "高")]
    st.table(high_high.reset_index(drop=True))

with col2:
    st.subheader("緊急度：低、重要度：高（計画を立てる）")
    high_low = st.session_state["tasks"][(st.session_state["tasks"]["重要度"] == "高") & (st.session_state["tasks"]["緊急度"] == "低")]
    st.table(high_low.reset_index(drop=True))

with col3:
    st.subheader("緊急度：高、重要度：低（委任する）")
    low_high = st.session_state["tasks"][(st.session_state["tasks"]["重要度"] == "低") & (st.session_state["tasks"]["緊急度"] == "高")]
    st.table(low_high.reset_index(drop=True))

with col4:
    st.subheader("緊急度：低、重要度：低（削除する）")
    low_low = st.session_state["tasks"][(st.session_state["tasks"]["重要度"] == "低") & (st.session_state["tasks"]["緊急度"] == "低")]
    st.table(low_low.reset_index(drop=True))

# コメント
st.write("""
**使い方**:
- タスクを直接マトリクスの表に入力・編集してください。
""")
