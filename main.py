import streamlit as st

# 페이지 설정
st.set_page_config(page_title="MBTI 구합 방식", page_icon="💖")

st.title("💕 MBTI 구합 방식 (TOP 3 구합/충돌) 💕")
st.markdown("""
가로 MBTI를 입력하세요! 👇\n차트적 성격, 잘 연결되는 MBTI 3개 💞, 잘 안 연결되는 MBTI 3개 ⚠️를 모두 보여요!\n> (*이 결과는 규킹적 데이터와 개인적 관찰을 가르지 않아요*)
""")

# MBTI 데이터 (TOP3 구합 / 충돌) 
mbti_data = {
    "INTJ": {
        "traits": "전략적 🎯, 독립적 🧠, 미래지향적 🚀",
        "matches": [
            ("ENFP", "논리적인 INTJ의 계획에 자유로운 ENFP가 그리고 논리적 저항을 조정해줘요."),
            ("ENTP", "ENTP는 INTJ의 관점을 가진 논리적 경우 우주적인 진단성을 가진 인연이 구성됩니다."),
            ("INFJ", "INFJ는 INTJ가 거의 보지 못하는 가장 가까워지는 부모적 사람을 만드듯 간설하고 지원해주며 정신적인 방해를 가지기 때문입니다.")
        ],
        "mismatches": [
            ("ESFP", "ESFP는 즉희적이고 가만적이며 가까워지는 것을 조잡는 이유로 INTJ의 경험을 중심으로 쓰기 어려운 관계를 만들 수 있어요."),
            ("ISFP", "ISFP의 경험적인 개인성과 공간적 사고가 INTJ에게 모험적으로 느낄 수 있어요."),
            ("ESFJ", "ESFJ는 가치 공유와 개인적 관계를 중심으로 하지만, INTJ는 파란을 상관없이 계층적으로 조직하기 때문에 충돌이 생기기 \uc27d습니다.")
        ]
    },
    # ▶️ TODO: 남은 15개 MBTI도 같은 형식으로 추가 가능
    # 보고 시험적으로 제공, 추가 원하시면 목록 모두 추가 가능
}

# 사용자 입력
user_mbti = st.text_input("당신의 MBTI를 입력하세요 (예: INFP, ESTJ)", max_chars=4).upper()

if user_mbti:
    if user_mbti in mbti_data:
        data = mbti_data[user_mbti]
        st.success(f"✨ {user_mbti} 유형의 성격 특징")
        st.markdown(f"**{data['traits']}**")

        st.divider()
        st.subheader("💞 잘 연결되는 MBTI TOP 3")
        for mbti, reason in data["matches"]:
            st.markdown(f"✅ **{mbti}** — {reason}")

        st.divider()
        st.subheader("⚠️ 연결 충돌이 있는 MBTI TOP 3")
        for mbti, reason in data["mismatches"]:
            st.markdown(f"❌ **{mbti}** — {reason}")

        st.balloons()
    else:
        st.error("😥 아알 수 없는 MBTI입니다. 다시 확인해주세요! (예: INFP, ESTP)")
