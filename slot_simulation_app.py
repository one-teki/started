import streamlit as st
import random
import pandas as pd

def simulate_slot(total_spins):
    results = []
    spins = 0
    big_count = 0
    reg_count = 0
    while spins < total_spins:
        spins += 1
        if random.randint(1, 255) == 1:
            result_type = random.choice(['BIG', 'REG'])
            if result_type == 'BIG':
                big_count += 1
            else:
                reg_count += 1
            results.append((spins, result_type))
    return results, big_count, reg_count

st.title('スロットシミュレーションアプリ')

# ユーザー入力
total_spins = st.number_input('シミュレーションする回転数を入力してください', min_value=1, value=1000)

# ボタンが押されたらシミュレーションを実行
if st.button('シミュレーション開始'):
    results, big_count, reg_count = simulate_slot(total_spins)
    if results:
        df = pd.DataFrame(results, columns=['回転数', '結果'])
        st.write('シミュレーション結果:', df)
        st.write(f'総回転数: {total_spins}')
        st.write(f'BIGの確率: {big_count / total_spins:.4f} (実際の確率: {1/255:.4f})')
        st.write(f'REGの確率: {reg_count / total_spins:.4f} (実際の確率: {1/255:.4f})')
        st.write(f'合算の確率: {(big_count + reg_count) / total_spins:.4f} (実際の確率: {2/255:.4f})')
    else:
        st.write('指定された回転数では当たりが出ませんでした。')
