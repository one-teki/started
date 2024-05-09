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
    </style>
""", unsafe_allow_html=True)

# タスクの入力セクション
with st.form("task_form"):
    task = st.text_input("タスクを入力してください", "")
    importance = st.selectbox("重要度", ["低", "高"])
    urgency = st.selectbox("緊急度", ["低", "高"])

    # フォームの送信ボタン
    submitted = st.form_submit_button("タスクを追加")

# タスクを保存するデータフレームをセッションステートで保持
if "tasks" not in st.session_state:
    st.session_state["tasks"] = pd.DataFrame(columns=["タスク", "重要度", "緊急度"])

# フォームが送信されたら、タスクをデータフレームに追加
if submitted and task:
    new_task = pd.DataFrame([[task, importance, urgency]], columns=["タスク", "重要度", "緊急度"])
    st.session_state["tasks"] = pd.concat([st.session_state["tasks"], new_task], ignore_index=True)

# アイゼンハワーのマトリクス表示
st.header("アイゼンハワーのマトリクス")
col1, col2 = st.columns([1, 1], gap="medium", key="col1_col2")
col3, col4 = st.columns([1, 1], gap="medium", key="col3_col4")

with col1:
    st.markdown('<div class="column1">', unsafe_allow_html=True)
    st.subheader("緊急度：高、重要度：高（今すぐ実行）")
    high_high = st.session_state["tasks"][(st.session_state["tasks"]["重要度"] == "高") & (st.session_state["tasks"]["緊急度"] == "高"])]
    st.table(high_high.reset_index(drop=True))
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="column2">', unsafe_allow_html=True)
    st.subheader("緊急度：低、重要度：高（計画を立てる）")
    high_low = st.session_state["tasks"][(st.session_state["tasks"]["重要度"] == "高") & (st.session_state["tasks"]["緊急度"] == "低"])]
    st.table(high_low.reset_index(drop=True))
    st.markdown('</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="column3">', unsafe_allow_html=True)
    st.subheader("緊急度：高、重要度：低（委任する）")
    low_high = st.session_state["tasks"][(st.session_state["tasks"]["重要度"] == "低") & (st.session_state["tasks"]["緊急度"] == "高"])]
    st.table(low_high.reset_index(drop=True))
    st.markdown('</div>', unsafe_allow_html=True)

with col4:
    st.markdown('<div class="column4">', unsafe_allow_html=True)
    st.subheader("緊急度：低、重要度：低（削除する）")
    low_low = st.session_state["tasks"][(st.session_state["tasks"]["重要度"] == "低") & (st.session_state["tasks"]["緊急度"] == "低"])]
    st.table(low_low.reset_index(drop=True))
    st.markdown('</div>', unsafe_allow_html=True)

# コメント
st.write("""
**使い方**:
- タスクを入力し、重要度と緊急度を選択してください。
- "タスクを追加"ボタンを押すと、タスクが追加され、アイゼンハワーのマトリクスに自動的に分類されます。
""")
