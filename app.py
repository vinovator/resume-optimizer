import streamlit as st
from src.crew import run_resume_crew

st.set_page_config(page_title="Resume Optimizer Pro", page_icon="👔", layout="wide")
st.title("👔 Resume Optimizer Pro")

col1, col2 = st.columns(2)
with col1:
    resume_input = st.text_area("Paste Resume:", height=200)
with col2:
    job_input = st.text_area("Paste Job Description:", height=200)


# --- THE CALLBACK FUNCTION ---
def step_callback(step_output):
    """
    This function is called by CrewAI every time an agent takes a step.
    We use it to update the Streamlit UI.
    """
    # CrewAI steps return a tuple or object. We extract the thought/action.
    # Note: Structure can vary slightly by version, this is robust.
    try:
        # Try to access the thought process
        thought = ""
        if hasattr(step_output, 'thought') and step_output.thought:
            thought = step_output.thought
        
        # If there is a tool input (delegation), show that too
        tool = ""
        if hasattr(step_output, 'tool') and step_output.tool:
            tool = f"Using tool: {step_output.tool}"
            
        # Write to the current Streamlit container (the st.status box)
        if thought:
            st.markdown(f"🤖 **Thinking:** {thought}")
        if tool:
            st.markdown(f"🔧 **Action:** {tool}")
            
    except Exception as e:
        st.write(f"Agent working... ({e})")



if st.button("Analyze Resume against JD"):
    if not resume_input or not job_input:
        st.warning("Please input data.")
    else:
        with st.status("🚀 Launching the Hiring Committee...", expanded=True) as status:
            try:
                result = run_resume_crew(
                    resume_input, 
                    job_input,
                    callback_function=step_callback
                )

                # Once finished, update the status box
                status.update(label="✅ Analysis Complete!", state="complete", expanded=False)
                data = result.pydantic
                
                # --- TOP LEVEL SCORE ---
                st.divider()
                st.markdown(f"<h1 style='text-align: center; color: #4CAF50;'>Match Score: {data.match_score}%</h1>", unsafe_allow_html=True)
                
                # --- DETAILED SCORES (New Section!) ---
                st.subheader("📊 Detailed Breakdown")
                c1, c2, c3, c4 = st.columns(4)
                c1.metric("Tech Skills", f"{data.hard_skills_score}%")
                c2.metric("Experience", f"{data.experience_score}%")
                c3.metric("Education", f"{data.education_score}%")
                c4.metric("Location", f"{data.location_score}%")
                
                # --- THE GAPS ---
                st.divider()
                col_left, col_right = st.columns(2)
                
                with col_left:
                    st.error("❌ Missing Hard Skills")
                    for item in data.missing_hard_skills:
                        st.write(f"- {item}")
                        
                    st.error("❌ Experience Gaps")
                    for item in data.missing_experience:
                        st.write(f"- {item}")

                with col_right:
                    st.warning("⚠️ Education / Location")
                    st.write(f"**Education:** {data.education_gap}")
                    st.write(f"**Location:** {data.location_status}")
                    
                    st.info("🧠 Soft Skills Gaps")
                    for item in data.missing_soft_skills:
                        st.write(f"- {item}")

                # --- THE FIX ---
                st.divider()
                st.subheader("✨ Optimized Summary")
                st.success(data.tailored_summary)
                
                st.subheader("💪 Improved Bullet Points")
                for bullet in data.improved_bullets:
                    st.markdown(f"> {bullet}")

            except Exception as e:
                st.error(f"Error: {e}")