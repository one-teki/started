import streamlit as st
import pandas as pd

# タイトル
st.title("アイゼンハワーのマトリクス（重要度-緊急度マトリクス）")

# 説明
st.write("""
このアプリを使って、タスクの優先順位を決定しましょう。
タスクを入力し、重要度と緊急度を選択することで、アイゼンハワーのマトリクスに自動的に分類されます。
""")

# カスタムCSSでカラムの幅を調整
st.markdown("""
    <style>
        .column1, .column2, .column3, .column4 {
            flex: 0 0 20em;
            max-width: 20em;
        }
        .clear-button {
            margin-top: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# セッションステートの初期化
if "tasks" not in st.session_state:
    st.session_state["tasks"] = pd.DataFrame(columns=["タスク", "重要度", "緊急度"])

# タスクの入力セクション
with st.form("task_form"):
    task = st.text_input("タスクを入力してください", value="", key="task")
    importance = st.selectbox("重要度", ["低", "高"], key="importance")
    urgency = st.selectbox("緊急度", ["低", "高"], key="urgency")

    # フォームの送信ボタン
    submitted = st.form_submit_button("タスクを追加")

# フォームが送信されたら、タスクをデータフレームに追加
if submitted and task:
    new_task = pd.DataFrame([[task, importance, urgency]], columns=["タスク", "重要度", "緊急度"])
    st.session_state["tasks"] = pd.concat([st.session_state["tasks"], new_task], ignore_index=True)

# アイゼンハワーのマトリクス表示
st.header("アイゼンハワーのマトリクス")
col1, col2 = st.columns([1, 1], gap="medium")
col3, col4 = st.columns([1, 1], gap="medium")

with col1:
    st.subheader("緊急度：高、重要度：高（今すぐ実行）")
    high_high = st.session_state["tasks"][(st.session_state["tasks"]["重要度"] == "高") & (st.session_state["tasks"]["緊急度"] == "高")]
    st.table(high_high.reset_index(drop=True))
    if st.button("クリア（今すぐ実行）", key="clear_high_high"):
        st.session_state["tasks"] = st.session_state["tasks"][
            (st.session_state["tasks"]["重要度"] != "高") | (st.session_state["tasks"]["緊急度"] != "高")
        ]

with col2:
    st.subheader("緊急度：低、重要度：高（計画を立てる）")
    high_low = st.session_state["tasks"][(st.session_state["tasks"]["重要度"] == "高") & (st.session_state["tasks"]["緊急度"] == "低")]
    st.table(high_low.reset_index(drop=True))
    if st.button("クリア（計画を立てる）", key="clear_high_low"):
        st.session_state["tasks"] = st.session_state["tasks"][
            (st.session_state["tasks"]["重要度"] != "高") | (st.session_state["tasks"]["緊急度"] != "低")
        ]

with col3:
    st.subheader("緊急度：高、重要度：低（委任する）")
    low_high = st.session_state["tasks"][(st.session_state["重要度"] == "低") & (st.session_state["緊急度"] == "高")]
    st.table(low_high.reset_index(drop=True))
    if st.button("クリア（委任する）", key="clear_low_high"):
        st.session_state["tasks"] = st.session_state["tasks"][
            (st.session_state["重要度"] != "低") | (st.session_state["緊急度"] != "高")
        ]

with col4:
    st.subheader("緊急度：低、重要度：低（削除する）")
    low_low = st.session_state["tasks"][(st.session_state["重要度"] == "低") & (st.session_state["緊急度"] == "低")]
    st.table(low_low.reset_index(drop=True))
    if st.button("クリア（削除する）", key="clear_low_low"):
        st.session_state["tasks"] = st.session_state["tasks"][
            (st.session_state["重要度"] != "低") | (st.session_state["緊急度"] != "低")
        ]

# 全タスク削除ボタン
if st.button("全タスク削除"):
    st.session_state["tasks"] = pd.DataFrame(columns=["タスク", "重要度", "緊急度"])

# コメント
st.write("""
**使い方**:
- タスクを入力し、重要度と緊急度を選択してください。
- "タスクを追加"ボタンを押すと、タスクが追加され、アイゼンハワーのマトリクスに自動的に分類されます。
- 各象限の「クリア」ボタンでその象限のタスクのみを削除できます。
- 「全タスク削除」ボタンで全ての象限のタスクを一括削除できます。
""")
