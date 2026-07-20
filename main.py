import streamlit as st

# ---------------------------------------------------------
# 페이지 설정
# ---------------------------------------------------------
st.set_page_config(
    page_title="MBTI 포켓몬 추천",
    page_icon="⚡",
    layout="centered",
)

# ---------------------------------------------------------
# MBTI별 추천 포켓몬 데이터
# ---------------------------------------------------------
pokemon_data = {
    "INTJ": {
        "pokemon": "뮤츠",
        "emoji": "🧬",
        "type": "에스퍼",
        "title": "독립적인 전략가",
        "description": (
            "높은 지능과 강한 독립심을 가진 뮤츠가 잘 어울립니다. "
            "혼자 깊이 생각하고, 자신만의 계획에 따라 움직이는 모습이 INTJ와 닮았습니다."
        ),
        "strength": "분석력 · 전략성 · 독립성",
        "color": "#8B5CF6",
        "quote": "복잡한 상황일수록 차분하게 답을 찾아내는 타입",
    },
    "INTP": {
        "pokemon": "후딘",
        "emoji": "🥄",
        "type": "에스퍼",
        "title": "호기심 많은 논리학자",
        "description": (
            "뛰어난 두뇌와 분석 능력을 지닌 후딘이 잘 어울립니다. "
            "끊임없이 원리를 탐구하고 논리적으로 문제를 해결하는 모습이 INTP와 비슷합니다."
        ),
        "strength": "논리력 · 탐구심 · 창의성",
        "color": "#7C3AED",
        "quote": "세상의 모든 원리를 알고 싶어 하는 타입",
    },
    "ENTJ": {
        "pokemon": "리자몽",
        "emoji": "🔥",
        "type": "불꽃 · 비행",
        "title": "강력한 지휘관",
        "description": (
            "강한 자신감과 추진력을 가진 리자몽이 잘 어울립니다. "
            "목표를 향해 거침없이 나아가고 주변을 이끄는 모습이 ENTJ와 닮았습니다."
        ),
        "strength": "리더십 · 결단력 · 추진력",
        "color": "#EF4444",
        "quote": "정한 목표는 반드시 이루어 내는 타입",
    },
    "ENTP": {
        "pokemon": "팬텀",
        "emoji": "👻",
        "type": "고스트 · 독",
        "title": "재치 있는 발명가",
        "description": (
            "장난기와 예측하기 어려운 매력을 가진 팬텀이 잘 어울립니다. "
            "새로운 아이디어를 즐기고 틀에 얽매이지 않는 모습이 ENTP와 비슷합니다."
        ),
        "strength": "재치 · 도전정신 · 아이디어",
        "color": "#6D28D9",
        "quote": "평범한 답보다 재미있는 가능성을 찾는 타입",
    },
    "INFJ": {
        "pokemon": "가디안",
        "emoji": "🔮",
        "type": "에스퍼 · 페어리",
        "title": "통찰력 있는 수호자",
        "description": (
            "상대의 감정을 이해하고 소중한 존재를 지키는 가디안이 잘 어울립니다. "
            "조용하지만 깊은 신념과 따뜻함을 지닌 모습이 INFJ와 닮았습니다."
        ),
        "strength": "통찰력 · 공감 · 신념",
        "color": "#10B981",
        "quote": "말하지 않아도 상대의 마음을 알아보는 타입",
    },
    "INFP": {
        "pokemon": "이브이",
        "emoji": "🌟",
        "type": "노말",
        "title": "가능성이 가득한 이상주의자",
        "description": (
            "다양한 모습으로 성장할 가능성을 가진 이브이가 잘 어울립니다. "
            "자신만의 가치와 꿈을 소중히 여기며 여러 가능성을 품은 모습이 INFP와 비슷합니다."
        ),
        "strength": "감수성 · 가치관 · 가능성",
        "color": "#F59E0B",
        "quote": "나만의 방식으로 특별하게 성장하는 타입",
    },
    "ENFJ": {
        "pokemon": "루카리오",
        "emoji": "💫",
        "type": "격투 · 강철",
        "title": "사람을 이끄는 조력자",
        "description": (
            "상대의 파동과 감정을 읽는 루카리오가 잘 어울립니다. "
            "사람을 이해하고 더 나은 방향으로 이끄는 따뜻한 리더십이 ENFJ와 닮았습니다."
        ),
        "strength": "공감력 · 리더십 · 책임감",
        "color": "#2563EB",
        "quote": "사람들의 잠재력을 발견하고 이끌어 주는 타입",
    },
    "ENFP": {
        "pokemon": "피카츄",
        "emoji": "⚡",
        "type": "전기",
        "title": "긍정적인 에너지 전도사",
        "description": (
            "밝고 친근하며 에너지가 넘치는 피카츄가 잘 어울립니다. "
            "새로운 만남과 모험을 즐기고 주변에 활력을 주는 모습이 ENFP와 비슷합니다."
        ),
        "strength": "열정 · 친화력 · 창의성",
        "color": "#EAB308",
        "quote": "어디서든 즐거운 가능성을 발견하는 타입",
    },
    "ISTJ": {
        "pokemon": "거북왕",
        "emoji": "💧",
        "type": "물",
        "title": "믿음직한 관리자",
        "description": (
            "단단한 방어력과 안정감을 가진 거북왕이 잘 어울립니다. "
            "맡은 일을 책임감 있게 수행하고 신뢰를 쌓아 가는 모습이 ISTJ와 닮았습니다."
        ),
        "strength": "책임감 · 신중함 · 꾸준함",
        "color": "#0284C7",
        "quote": "약속한 일은 끝까지 책임지는 타입",
    },
    "ISFJ": {
        "pokemon": "해피너스",
        "emoji": "💗",
        "type": "노말",
        "title": "따뜻하고 다정한 수호자",
        "description": (
            "다친 친구를 정성껏 돌보는 해피너스가 잘 어울립니다. "
            "세심하게 주변을 살피고 묵묵히 도움을 주는 모습이 ISFJ와 비슷합니다."
        ),
        "strength": "배려 · 성실함 · 헌신",
        "color": "#EC4899",
        "quote": "작은 부분까지 따뜻하게 챙겨 주는 타입",
    },
    "ESTJ": {
        "pokemon": "윈디",
        "emoji": "🦁",
        "type": "불꽃",
        "title": "당당하고 믿음직한 리더",
        "description": (
            "용감하고 충성심이 강한 윈디가 잘 어울립니다. "
            "질서와 책임을 중요하게 생각하며 신속하게 행동하는 모습이 ESTJ와 닮았습니다."
        ),
        "strength": "실행력 · 책임감 · 조직력",
        "color": "#F97316",
        "quote": "해야 할 일을 정확하고 빠르게 처리하는 타입",
    },
    "ESFJ": {
        "pokemon": "님피아",
        "emoji": "🎀",
        "type": "페어리",
        "title": "다정한 분위기 메이커",
        "description": (
            "친밀한 유대감을 중요하게 여기는 님피아가 잘 어울립니다. "
            "사람들과 어울리며 모두가 편안하도록 세심하게 챙기는 모습이 ESFJ와 비슷합니다."
        ),
        "strength": "친화력 · 배려 · 협동심",
        "color": "#DB2777",
        "quote": "모두가 행복한 분위기를 만드는 타입",
    },
    "ISTP": {
        "pokemon": "개굴닌자",
        "emoji": "🥷",
        "type": "물 · 악",
        "title": "침착한 만능 해결사",
        "description": (
            "빠른 판단력과 뛰어난 기술을 가진 개굴닌자가 잘 어울립니다. "
            "말보다 행동으로 문제를 해결하고 상황에 유연하게 대처하는 모습이 ISTP와 닮았습니다."
        ),
        "strength": "순발력 · 실용성 · 문제 해결",
        "color": "#1D4ED8",
        "quote": "필요한 순간에 실력으로 보여 주는 타입",
    },
    "ISFP": {
        "pokemon": "세레비",
        "emoji": "🍃",
        "type": "에스퍼 · 풀",
        "title": "자유로운 감성 탐험가",
        "description": (
            "자연과 조화를 이루며 자유롭게 여행하는 세레비가 잘 어울립니다. "
            "부드러운 감성과 자신만의 아름다움을 중요하게 여기는 모습이 ISFP와 비슷합니다."
        ),
        "strength": "감수성 · 유연함 · 예술성",
        "color": "#22C55E",
        "quote": "조용히 자신만의 아름다운 길을 걷는 타입",
    },
    "ESTP": {
        "pokemon": "에이스번",
        "emoji": "⚽",
        "type": "불꽃",
        "title": "대담한 행동파",
        "description": (
            "빠르고 자신감 넘치는 에이스번이 잘 어울립니다. "
            "순간을 즐기며 과감하게 도전하고 현장에서 능력을 발휘하는 모습이 ESTP와 닮았습니다."
        ),
        "strength": "행동력 · 적응력 · 자신감",
        "color": "#DC2626",
        "quote": "고민하기보다 직접 뛰어들어 답을 찾는 타입",
    },
    "ESFP": {
        "pokemon": "파치리스",
        "emoji": "🎉",
        "type": "전기",
        "title": "사랑스러운 엔터테이너",
        "description": (
            "활발하고 사랑스러운 파치리스가 잘 어울립니다. "
            "사람들과 즐거움을 나누고 어디서든 밝은 분위기를 만드는 모습이 ESFP와 비슷합니다."
        ),
        "strength": "낙천성 · 표현력 · 사교성",
        "color": "#06B6D4",
        "quote": "평범한 순간도 즐거운 추억으로 만드는 타입",
    },
}

# ---------------------------------------------------------
# 디자인
# ---------------------------------------------------------
st.markdown(
    """
    <style>
        .stApp {
            background:
                radial-gradient(circle at 10% 10%, #fff7cc 0%, transparent 25%),
                radial-gradient(circle at 90% 20%, #dbeafe 0%, transparent 28%),
                linear-gradient(135deg, #fffdf5 0%, #f4f7ff 100%);
        }

        .block-container {
            max-width: 760px;
            padding-top: 2.3rem;
            padding-bottom: 3rem;
        }

        .main-title {
            text-align: center;
            font-size: 2.7rem;
            font-weight: 900;
            color: #222222;
            margin-bottom: 0.25rem;
        }

        .sub-title {
            text-align: center;
            color: #626262;
            font-size: 1.05rem;
            margin-bottom: 2rem;
        }

        .pokeball {
            text-align: center;
            font-size: 4.2rem;
            margin-bottom: 0.2rem;
            animation: bounce 1.8s infinite;
        }

        @keyframes bounce {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-8px); }
        }

        div[data-testid="stSelectbox"] label {
            font-size: 1.1rem;
            font-weight: 700;
        }

        div.stButton > button {
            width: 100%;
            border: none;
            border-radius: 14px;
            padding: 0.8rem;
            font-size: 1.1rem;
            font-weight: 800;
            color: white;
            background: linear-gradient(90deg, #ef4444, #f97316);
            box-shadow: 0 7px 18px rgba(239, 68, 68, 0.22);
            transition: 0.2s;
        }

        div.stButton > button:hover {
            color: white;
            border: none;
            transform: translateY(-2px);
            box-shadow: 0 10px 22px rgba(239, 68, 68, 0.3);
        }

        .result-card {
            margin-top: 1.5rem;
            padding: 2rem;
            border-radius: 24px;
            color: white;
            text-align: center;
            box-shadow: 0 14px 35px rgba(0, 0, 0, 0.14);
        }

        .pokemon-emoji {
            font-size: 5rem;
            line-height: 1.2;
        }

        .match-label {
            display: inline-block;
            padding: 0.35rem 0.9rem;
            margin-top: 0.8rem;
            border-radius: 999px;
            background-color: rgba(255, 255, 255, 0.22);
            font-weight: 700;
        }

        .pokemon-name {
            font-size: 2.8rem;
            font-weight: 900;
            margin: 0.5rem 0 0.1rem 0;
        }

        .pokemon-type {
            font-size: 1rem;
            opacity: 0.9;
        }

        .pokemon-title {
            font-size: 1.35rem;
            font-weight: 800;
            margin-top: 1.2rem;
        }

        .description-box {
            background-color: rgba(255, 255, 255, 0.16);
            border-radius: 15px;
            padding: 1rem;
            margin-top: 1rem;
            line-height: 1.75;
            text-align: left;
        }

        .strength-box {
            margin-top: 1rem;
            font-weight: 700;
        }

        .quote-box {
            margin-top: 1rem;
            font-size: 1.05rem;
            font-style: italic;
            opacity: 0.95;
        }

        .footer {
            text-align: center;
            color: #777777;
            font-size: 0.85rem;
            margin-top: 2.5rem;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------
# 화면 구성
# ---------------------------------------------------------
st.markdown('<div class="pokeball">🔴</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="main-title">나와 닮은 포켓몬은?</div>',
    unsafe_allow_html=True,
)
st.markdown(
    '<div class="sub-title">MBTI를 선택하면 나와 어울리는 포켓몬을 추천해 드려요!</div>',
    unsafe_allow_html=True,
)

mbti_groups = {
    "분석가형": ["INTJ", "INTP", "ENTJ", "ENTP"],
    "외교관형": ["INFJ", "INFP", "ENFJ", "ENFP"],
    "관리자형": ["ISTJ", "ISFJ", "ESTJ", "ESFJ"],
    "탐험가형": ["ISTP", "ISFP", "ESTP", "ESFP"],
}

mbti_options = ["MBTI를 선택하세요"]
for group, types in mbti_groups.items():
    for mbti_type in types:
        mbti_options.append(f"{mbti_type} · {group}")

selected_option = st.selectbox(
    "당신의 MBTI는 무엇인가요?",
    mbti_options,
)

recommend_button = st.button("내 포켓몬 확인하기 ⚡")

# ---------------------------------------------------------
# 추천 결과
# ---------------------------------------------------------
if recommend_button:
    if selected_option == "MBTI를 선택하세요":
        st.warning("먼저 MBTI를 선택해 주세요.")
    else:
        selected_mbti = selected_option.split(" · ")[0]
        result = pokemon_data[selected_mbti]

        st.balloons()

        st.markdown(
            f"""
            <div class="result-card"
                 style="background: linear-gradient(
                     135deg,
                     {result["color"]},
                     #1f2937
                 );">
                <div class="pokemon-emoji">{result["emoji"]}</div>
                <div class="match-label">{selected_mbti}와 어울리는 포켓몬</div>
                <div class="pokemon-name">{result["pokemon"]}</div>
                <div class="pokemon-type">타입: {result["type"]}</div>
                <div class="pokemon-title">{result["title"]}</div>

                <div class="description-box">
                    {result["description"]}
                </div>

                <div class="strength-box">
                    ✨ 닮은 특성: {result["strength"]}
                </div>

                <div class="quote-box">
                    “{result["quote"]}”
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.markdown(
    """
    <div class="footer">
        MBTI와 포켓몬의 연결은 재미를 위한 추천이며 과학적 성격 검사가 아닙니다.
    </div>
    """,
    unsafe_allow_html=True,
)
