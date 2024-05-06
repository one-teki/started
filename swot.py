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

    # 戦略の提案
    st.header("戦略の提案")

    # SO戦略 (Maxi-Maxi)
    st.subheader("SO戦略 (強み × 機会)")
    so_strategy = f"""
    - {strengths.strip().splitlines()[0] if strengths.strip() else "強みを活用"} を活かして {opportunities.strip().splitlines()[0] if opportunities.strip() else "機会を捉える"} 戦略
    """
    st.write(so_strategy)

    # ST戦略 (Maxi-Mini)
    st.subheader("ST戦略 (強み × 脅威)")
    st_strategy = f"""
    - {strengths.strip().splitlines()[0] if strengths.strip() else "強みを活用"} を活かして {threats.strip().splitlines()[0] if threats.strip() else "脅威を軽減"} 戦略
    """
    st.write(st_strategy)

    # WO戦略 (Mini-Maxi)
    st.subheader("WO戦略 (弱み × 機会)")
    wo_strategy = f"""
    - {weaknesses.strip().splitlines()[0] if weaknesses.strip() else "弱みを克服"} して {opportunities.strip().splitlines()[0] if opportunities.strip() else "機会を活かす"} 戦略
    """
    st.write(wo_strategy)

    # WT戦略 (Mini-Mini)
    st.subheader("WT戦略 (弱み × 脅威)")
    wt_strategy = f"""
    - {weaknesses.strip().splitlines()[0] if weaknesses.strip() else "弱みを克服"} して {threats.strip().splitlines()[0] if threats.strip() else "脅威を軽減"} 戦略
    """
    st.write(wt_strategy)

    st.write("""
    **使い方**:
    - 提案された戦略を基に、具体的なアクションプランを作成しましょう。
    - SMARTフレームワークを使って、戦略を具体的な目標に落とし込むことをお勧めします。
    - "戦略の提案" セクションで出てきた内容をプロジェクトやビジネスに活かしていきましょう。
    """)

