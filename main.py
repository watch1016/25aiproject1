import streamlit as st

st.set_page_config(page_title="MBTI 궁합 분석기", page_icon="💖", layout="centered")

st.title("🔮 MBTI 궁합 분석기")
st.markdown("""
당신의 **MBTI**를 입력해보세요!  
💞 어울리는 MBTI TOP 3  
⚠️ 어울리지 않는 MBTI TOP 3  
이유와 함께 알려드릴게요 😄  
""")

mbti_data = {
    "INTJ": {
        "traits": "전략적 🎯, 독립적 🧠, 미래지향적 🚀",
        "matches": [
            ("ENFP", "자유롭고 감성적인 ENFP는 INTJ의 균형을 맞춰줍니다."),
            ("ENTP", "창의적이며 도전적인 ENTP는 지적인 자극을 줍니다."),
            ("INFJ", "비슷한 가치관과 깊이를 가진 INFJ와는 안정적인 관계를 형성합니다.")
        ],
        "mismatches": [
            ("ESFP", "즉흥적인 ESFP는 INTJ에게 피곤할 수 있어요."),
            ("ISFP", "감정 중심인 ISFP는 INTJ와 가치 충돌 가능성이 높아요."),
            ("ESTP", "감각 중심의 ESTP는 INTJ의 사고 중심과 충돌할 수 있어요.")
        ]
    },
    "INTP": {
        "traits": "논리적 🧩, 분석적 🔬, 호기심 많은 🤔",
        "matches": [
            ("ENTJ", "리더십 있는 ENTJ가 INTP의 아이디어를 현실화해 줍니다."),
            ("ENFP", "창의적이고 감정적인 ENFP는 INTP에게 새로운 시야를 줍니다."),
            ("INFJ", "깊이 있는 INFJ와는 철학적 대화로 잘 통합니다.")
        ],
        "mismatches": [
            ("ESFJ", "감정 중심적인 ESFJ는 INTP에게 피곤할 수 있어요."),
            ("ESTJ", "현실적이고 조직적인 ESTJ는 자유로운 INTP에게 억압적으로 느껴질 수 있어요."),
            ("ISFJ", "보수적인 ISFJ는 새로운 걸 탐구하려는 INTP와 갈등할 수 있어요.")
        ]
    },
    "ENTJ": {
        "traits": "리더십 강함 👑, 목표지향적 🏁, 결단력 있는 💥",
        "matches": [
            ("INTP", "창의적 아이디어를 실행하는 데 도움을 주는 파트너입니다."),
            ("ENFP", "열정적인 ENFP는 ENTJ에게 활력을 줍니다."),
            ("INFJ", "이상과 비전을 공유하며 성장할 수 있습니다.")
        ],
        "mismatches": [
            ("ISFP", "느긋한 ISFP는 ENTJ의 성향과 맞지 않습니다."),
            ("INFP", "감성 중심의 INFP는 ENTJ의 논리 중심과 충돌합니다."),
            ("ESFP", "즉흥적인 ESFP는 ENTJ에게 산만하게 느껴질 수 있어요.")
        ]
    },
    "ENTP": {
        "traits": "창의적 💡, 유쾌함 😄, 도전적 🗣️",
        "matches": [
            ("INFJ", "심리적으로 안정감을 줍니다."),
            ("INTJ", "논리적인 사고로 자극을 주고받을 수 있어요."),
            ("ENFP", "서로의 아이디어를 키워나가는 동반자입니다.")
        ],
        "mismatches": [
            ("ISFJ", "보수적인 ISFJ는 자유로운 ENTP에게 제약이 됩니다."),
            ("ISTJ", "계획적인 ISTJ와 즉흥적인 ENTP는 마찰이 많습니다."),
            ("ESFJ", "감성 중심의 ESFJ는 토론을 즐기는 ENTP와 갈등할 수 있어요.")
        ]
    },
    "INFJ": {
        "traits": "이상주의자 🌟, 직관적 🔮, 따뜻한 리더 💗",
        "matches": [
            ("ENFP", "자유롭고 낙천적인 ENFP는 INFJ에게 활력을 줍니다."),
            ("INFP", "깊이 있는 내면의 교감이 가능합니다."),
            ("ENFJ", "비슷한 가치와 목표로 함께 성장할 수 있어요.")
        ],
        "mismatches": [
            ("ESTP", "즉흥적인 ESTP는 INFJ에게 스트레스를 줍니다."),
            ("ESFP", "표면적인 대화를 선호하는 ESFP는 INFJ와 깊이 다를 수 있어요."),
            ("ENTP", "지속적인 논쟁은 감정적 INFJ에게 부담일 수 있습니다.")
        ]
    },
    "INFP": {
        "traits": "감성적 💞, 상상력 풍부 🎨, 조용한 이상주의자 🌈",
        "matches": [
            ("ENFJ", "감정적인 지지를 잘 해주는 파트너입니다."),
            ("INFJ", "비슷한 내면 세계로 깊은 관계 형성이 가능합니다."),
            ("ENFP", "서로의 감성을 존중하고 성장할 수 있어요.")
        ],
        "mismatches": [
            ("ESTJ", "현실적이고 직설적인 성향이 충돌할 수 있어요."),
            ("ENTJ", "효율을 추구하는 ENTJ는 감성적인 INFP를 이해하기 어려울 수 있어요."),
            ("ESTP", "즉흥적이고 겉도는 대화 스타일이 부담일 수 있어요.")
        ]
    },
    "ENFJ": {
        "traits": "타인 배려 ❤️, 사교적 🤝, 열정적 🔥",
        "matches": [
            ("INFP", "감성적으로 깊은 관계를 형성할 수 있어요."),
            ("INFJ", "가치관이 잘 맞아 협력적입니다."),
            ("ENFP", "낙천적인 에너지와 공감능력이 잘 맞아요.")
        ],
        "mismatches": [
            ("ISTP", "무뚝뚝한 ISTP는 ENFJ에게 감정적으로 부족할 수 있어요."),
            ("ESTP", "즉흥적인 성향은 ENFJ의 계획성과 충돌할 수 있습니다."),
            ("ISTJ", "감정보다 논리를 우선하는 ISTJ와는 거리감이 있습니다.")
        ]
    },
    "ENFP": {
        "traits": "에너지 넘침 ⚡, 창의적 💭, 사람 좋아함 🤗",
        "matches": [
            ("INFJ", "차분하고 따뜻한 INFJ는 ENFP의 좋은 반려자가 됩니다."),
            ("INFP", "감정적 이해와 창의성이 잘 맞아요."),
            ("INTJ", "이성과 감성이 균형을 이룹니다.")
        ],
        "mismatches": [
            ("ISTJ", "보수적이고 계획적인 ISTJ는 ENFP에게 답답할 수 있어요."),
            ("ESTJ", "논리와 효율 중심의 ESTJ는 감정적인 ENFP를 이해하기 어려워요."),
            ("ISTP", "감정 표현이 적은 ISTP는 ENFP에게 외롭게 느껴질 수 있어요.")
        ]
    },
    "ISTJ": {
        "traits": "신중함 📏, 책임감 🧱, 조직적 📊",
        "matches": [
            ("ESFP", "즐거운 에너지가 ISTJ를 활기차게 만듭니다."),
            ("ISFJ", "비슷한 성향으로 안정된 관계 형성 가능."),
            ("ESTJ", "실용적인 가치관과 책임감이 잘 맞아요.")
        ],
        "mismatches": [
            ("ENFP", "자유로운 사고방식이 부담이 될 수 있어요."),
            ("ENTP", "즉흥성과 토론을 좋아하는 성향은 충돌을 야기할 수 있어요."),
            ("INFP", "감성적인 INFP는 ISTJ의 직설적 성향에 상처받을 수 있어요.")
        ]
    },
    "ISFJ": {
        "traits": "배려심 🧸, 성실함 🧼, 안정 추구 🛏️",
        "matches": [
            ("ESTP", "활기찬 ESTP는 ISFJ에게 새로운 자극을 줍니다."),
            ("ESFP", "즐거움을 함께 누릴 수 있어요."),
            ("ISTJ", "같은 내향적 실용성향으로 안정적인 관계가 가능합니다.")
        ],
        "mismatches": [
            ("ENTP", "지적이고 논쟁적인 ENTP는 감정적인 ISFJ에게 어렵게 느껴질 수 있어요."),
            ("INTP", "감정보다는 논리에 집중하는 INTP와는 정서적 교류가 부족할 수 있어요."),
            ("ENFP", "예측 불가능한 행동은 ISFJ에게 불안감을 줄 수 있어요.")
        ]
    },
    "ESTJ": {
        "traits": "리더십 💼, 체계적 🧠, 냉정한 판단력 🧭",
        "matches": [
            ("ISFJ", "책임감 있는 파트너로 잘 맞습니다."),
            ("ISTJ", "실용주의적 성향으로 협력적입니다."),
            ("ESFJ", "조직적이며 신중한 점에서 유사성을 가집니다.")
        ],
        "mismatches": [
            ("INFP", "감성적이고 이상주의적인 성향이 부딪힐 수 있어요."),
            ("ENFP", "감정 중심의 의사결정은 ESTJ에게 비효율적으로 보일 수 있어요."),
            ("ISFP", "즉흥적이고 감정 중심의 ISFP와는 충돌 가능성이 높아요.")
        ]
    },
    "ESFJ": {
        "traits": "사교성 💬, 친절함 😊, 협동심 🤝",
        "matches": [
            ("ISFP", "서로를 배려하며 감성적으로 연결됩니다."),
            ("ISTJ", "조화롭게 협력할 수 있는 유형입니다."),
            ("ESFP", "같은 외향성과 감정 중심으로 쉽게 가까워질 수 있어요.")
        ],
        "mismatches": [
            ("INTP", "논리 중심의 사고방식은 감정 중심인 ESFJ와 충돌할 수 있어요."),
            ("ENTP", "지속적인 논쟁과 유쾌함이 ESFJ에게 피곤할 수 있어요."),
            ("INTJ", "감정적 교류가 부족하여 거리감이 생길 수 있습니다.")
        ]
    },
    "ISTP": {
        "traits": "논리적 🧠, 현실적 🔧, 독립적 🧍",
        "matches": [
            ("ESFP", "즐거움과 감각적 자극을 함께 나눌 수 있어요."),
            ("ESTP", "같은 탐험적 기질로 쉽게 통합니다."),
            ("ISFP", "서로 간섭 없이 편안한 관계를 형성할 수 있어요.")
        ],
        "mismatches": [
            ("ENFJ", "감정 표현이 많은 ENFJ는 ISTP에게 부담일 수 있어요."),
            ("ESFJ", "감성적 기대는 ISTP에게 스트레스를 줄 수 있어요."),
            ("ENFP", "지속적인 감정 교류 요구는 ISTP에게 피로감을 줄 수 있어요.")
        ]
    },
    "ISFP": {
        "traits": "감성적 🎨, 조용함 🌿, 유연함 🍃",
        "matches": [
            ("ESFJ", "배려심 깊은 ESFJ는 ISFP를 따뜻하게 감쌀 수 있어요."),
            ("ESTJ", "책임감 강한 ESTJ는 ISFP에게 안정감을 줍니다."),
            ("ISTP", "자율적인 관계를 지향하는 점에서 잘 맞아요.")
        ],
        "mismatches": [
            ("ENTJ", "성취 중심의 ENTJ는 ISFP에게 스트레스가 될 수 있어요."),
            ("ESTP", "과도한 활동성은 조용한 ISFP에게 부담입니다."),
            ("INTJ", "논리 중심 사고는 감성적 ISFP와 충돌할 수 있어요.")
        ]
    },
    "ESTP": {
        "traits": "활동적 🏍️, 현실적 🛠️, 즉흥적 🎯",
        "matches": [
            ("ISFJ", "조용한 ISFJ는 ESTP에게 안정을 줍니다."),
            ("ISTP", "비슷한 현실 중심 사고로 잘 맞습니다."),
            ("ESFP", "함께 즐기는 활동이 많아 유쾌한 관계가 가능합니다.")
        ],
        "mismatches": [
            ("INFJ", "깊은 감성적 교류는 ESTP에게 어렵게 느껴질 수 있어요."),
            ("INFP", "이상주의적이며 감성적인 성향과 충돌할 수 있어요."),
            ("ENFJ", "계획적이고 감정 표현이 많은 ENFJ는 부담일 수 있어요.")
        ]
    },
    "ESFP": {
        "traits": "사교적 🎤, 즉흥적 🎈, 활발함 💃",
        "matches": [
            ("ISTJ", "신중하고 책임감 있는 ISTJ는 ESFP에게 안정감을 줍니다."),
            ("ISFJ", "따뜻하고 배려심 있는 ISFJ는 ESFP와 조화를 이룹니다."),
            ("ESTP", "비슷한 활동 중심의 사고로 잘 맞아요.")
        ],
        "mismatches": [
            ("INTJ", "논리 중심 사고방식은 감성적인 ESFP에게 부담이 될 수 있어요."),
            ("INTP", "감정적 교류 부족은 ESFP에게 외로움을 줄 수 있어요."),
            ("INFJ", "깊은 내면 성찰은 ESFP에게 어렵게 느껴질 수 있어요.")
        ]
    }
}

user_mbti = st.text_input("당신의 MBTI를 입력하세요 (예: INFP)", max_chars=4).upper()

if user_mbti:
    if user_mbti in mbti_data:
        data = mbti_data[user_mbti]
        st.success(f"✨ {user_mbti}의 특징: {data['traits']}")

        st.subheader("💞 잘 어울리는 MBTI TOP 3")
        for mbti, reason in data["matches"]:
            st.markdown(f"✅ **{mbti}** — {reason}")

        st.divider()

        st.subheader("⚠️ 잘 안 어울리는 MBTI TOP 3")
        for mbti, reason in data["mismatches"]:
            st.markdown(f"🚫 **{mbti}** — {reason}")

        st.balloons()
    else:
        st.error("입력한 MBTI를 찾을 수 없습니다. 예: INFP, ESTJ 등 올바른 형식으로 입력해주세요.")
