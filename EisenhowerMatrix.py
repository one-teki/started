import streamlit as st
import pandas as pd

# タイトル
st.title("Eisenhower Matrix (Importance-Urgency Matrix)")

# 説明
st.write("""
Use this app to prioritize your tasks.
Input tasks and select their importance and urgency, and they will automatically be categorized in the Eisenhower Matrix.
""")

# セッションステートの初期化
if "tasks" not in st.session_state:
    st.session_state["tasks"] = pd.DataFrame(columns=["Task", "Importance", "Urgency"])

if "task_input" not in st.session_state:
    st.session_state["task_input"] = ""

if "importance" not in st.session_state:
    st.session_state["importance"] = "Low"

if "urgency" not in st.session_state:
    st.session_state["urgency"] = "Low"

# タスク入力リセット関数
def reset_task_input():
    st.session_state["task_input"] = ""

# タスクの入力セクション
with st.form("task_form"):
    task_input = st.text_input("Enter a task", st.session_state["task_input"], key="task_input")
    importance = st.selectbox("Importance", ["Low", "High"], key="importance")
    urgency = st.selectbox("Urgency", ["Low", "High"], key="urgency")

    # フォームの送信ボタン
    submitted = st.form_submit_button("Add Task", on_click=reset_task_input)

# フォームが送信されたら、タスクをデータフレームに追加
if submitted and task_input:
    new_task = pd.DataFrame([[task_input, importance, urgency]], columns=["Task", "Importance", "Urgency"])
    st.session_state["tasks"] = pd.concat([st.session_state["tasks"], new_task], ignore_index=True)

# 関数：テーブルの表示
def display_dataframe(df):
    if df.empty:
        st.write("empty")
    else:
        df.index = range(1, len(df) + 1)  # インデックス番号を1から始める
        st.dataframe(df.style.set_properties(**{'text-align': 'left'}).set_table_styles([{'selector': 'th', 'props': [('text-align', 'left')]}]), width=700)

# アイゼンハワーのマトリクス表示
st.header("Eisenhower Matrix")
col1, col2 = st.columns(2)
with col1:
    st.subheader("Urgency: High, Importance: High (Do Now)")
    high_high = st.session_state["tasks"][(st.session_state["tasks"]["Importance"] == "High") & (st.session_state["tasks"]["Urgency"] == "High")]
    display_dataframe(high_high)

with col2:
    st.subheader("Urgency: Low, Importance: High (Plan)")
    high_low = st.session_state["tasks"][(st.session_state["tasks"]["Importance"] == "High") & (st.session_state["tasks"]["Urgency"] == "Low")]
    display_dataframe(high_low)

col3, col4 = st.columns(2)
with col3:
    st.subheader("Urgency: High, Importance: Low (Delegate)")
    low_high = st.session_state["tasks"][(st.session_state["tasks"]["Importance"] == "Low") & (st.session_state["tasks"]["Urgency"] == "High")]
    display_dataframe(low_high)

with col4:
    st.subheader("Urgency: Low, Importance: Low (Delete)")
    low_low = st.session_state["tasks"][(st.session_state["tasks"]["Importance"] == "Low") & (st.session_state["tasks"]["Urgency"] == "Low")]
    display_dataframe(low_low)

# コメント
st.write("""
**How to use**:
- Enter a task and select its importance and urgency.
- Click the "Add Task" button, and the task will be categorized in the Eisenhower Matrix.
""")
