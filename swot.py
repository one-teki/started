import streamlit as st

# タイトル
st.title("SWOT分析アプリ")

# 説明
st.write("""
このアプリを使って、あなたのプロジェクトやビジネスのSWOT分析を行いましょう。
""")

# フォームの作成
with st.form("swot_form"):
    st.subheader("Strengths（強み）")
    strengths = st.text_area("あなたのビジネスやプロジェクトの強みを入力してください", "")

    st.subheader("Weaknesses（弱み）")
    weaknesses = st.text_area("あなたのビジネスやプロジェクトの弱みを入力してください", "")

    st.subheader("Opportunities（機会）")
    opportunities = st.text_area("あなたのビジネスやプロジェクトにおける機会を入力してください", "")

    st.subheader("Threats（脅威）")
    threats = st.text_area("あなたのビジネスやプロジェクトにおける脅威を入力してください", "")

    # フォームの送信ボタン
    submitted = st.form_submit_button("SWOT分析を表示")

# 送信ボタンが押されたら、結果を表示
if submitted:
    st.header("SWOT分析結果")

    # カラムの分割
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Strengths（強み）")
        st.write(strengths)

    with col2:
        st.subheader("Weaknesses（弱み）")
        st.write(weaknesses)

    col3, col4 = st.columns(2)

    with col3:
        st.subheader("Opportunities（機会）")
        st.write(opportunities)

    with col4:
        st.subheader("Threats（脅威）")
        st.write(threats)

# コメント
st.write("""
**使い方**:
- まず、各カテゴリーに対応する内容を入力してください。
- "SWOT分析を表示"ボタンを押すと、入力された内容が表示されます。
- 結果をコピーして他のドキュメントに貼り付けたり、スクリーンショットを撮って共有したりできます。
""")
