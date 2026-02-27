import streamlit as st
from backend import compute_similarity, risk_analysis, collaboration_score
from database import startups

st.set_page_config(page_title="AI Startup–Industry Matchmaker", layout="wide")

st.title("🚀 AI Startup–Industry Collaboration Matchmaker")
st.markdown("### Intelligent Compatibility & Risk-Based Ranking System")

# -------- Industry Input --------
st.header("🏢 Industry Requirements")

industry_problem = st.text_area("Describe Industry Problem Statement")
industry_tech = st.text_input("Required Technologies (comma separated)")
industry_budget = st.selectbox("Budget Range", ["Low", "Medium", "High"])

if st.button("🔍 Find Best Startup Matches"):

    if industry_problem and industry_tech:

        industry_text = industry_problem + " " + industry_tech

        results = []

        for startup in startups:

            startup_text = startup["domain"] + " " + startup["tech"]

            match_percentage = compute_similarity(industry_text, startup_text)
            risk_score = risk_analysis(startup["stage"])
            final_score = collaboration_score(match_percentage, risk_score)

            results.append({
                "Startup": startup["name"],
                "Match %": match_percentage,
                "Risk Score": risk_score,
                "Final Collaboration Score": final_score,
                "Stage": startup["stage"]
            })

        # Rank startups
        ranked_results = sorted(results, key=lambda x: x["Final Collaboration Score"], reverse=True)

        st.subheader("📊 Ranked Startup Recommendations")

        for idx, result in enumerate(ranked_results):

            st.markdown(f"## 🏆 Rank {idx+1}: {result['Startup']}")

            col1, col2, col3 = st.columns(3)
            col1.metric("Match %", f"{result['Match %']}%")
            col2.metric("Risk Score", result["Risk Score"])
            col3.metric("Final Score", result["Final Collaboration Score"])

            if result["Final Collaboration Score"] > 70:
                st.success("🔥 Highly Recommended for Immediate Collaboration")
            elif result["Final Collaboration Score"] > 40:
                st.warning("⚡ Moderate Potential – Further Evaluation Needed")
            else:
                st.error("❌ Low Alignment")

            st.markdown("---")

        st.markdown("### 📈 Future Scope Enhancements")
        st.write("- API-based deployment")
        st.write("- Real startup database integration")
        st.write("- AI-powered success prediction model")
        st.write("- Blockchain-based smart contract system")

    else:
        st.warning("Please fill Industry Problem and Technologies.")
