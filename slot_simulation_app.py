import streamlit as st
import random

def simulate_slot(total_spins):
    results = []
    spins = 0
    while spins < total_spins:
        spins += 1
        if random.randint(1, 255) == 1:
            if random.choice(['BIG', 'REG']) == 'BIG':
                results.append((spins, 'BIG'))
            else:
                results.append((spins, 'REG'))
            spins = 0  # リセットして次の当たりまでの回数をカウント
    return results

st.title('スロットシミュレーションアプリ')

# ユーザー入力
total_spins = st.number_input('シミュレーションする回転数を入力してください', min_value=1, value=1000)

# ボタンが押されたらシミュレーションを実行
if st.button('シミュレーション開始'):
    results = simulate_slot(total_spins)
    if results:
        st.write('当たりが出た回転数と種類:')
        for spin, result in results:
            st.write(f'{spin}回転目: {result}')
        st.write(f'総回転数: {total_spins}')
        st.write(f'試行回数: {len(results)}')
    else:
        st.write('指定された回転数では当たりが出ませんでした。')

