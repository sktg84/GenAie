import streamlit as st
import base64


def enter_key_widget():
    st.set_page_config(page_title="Test GenAie powered by Gemini Pro", page_icon="🧞‍♂️")
    left_co, cent_co, last_co = st.columns([1, 3, 1])

    with cent_co:
        st.image("testGenie.jpg", width=400)
        st.markdown(
            "<h3 style='text-align: center;'>Gen-AI Test Plan Writer</h3>",
            unsafe_allow_html=True,
        )

    with st.expander("Provide Your Google API Key or Type Demo"):
        google_api_key = st.text_input(
            "Google API Key", key="google_api_key", type="password"
        )

    st.divider()
    if "Demo" in google_api_key:
        return st.secrets["API_KEY"]

    if not google_api_key:
        st.info("Enter your Google API Key or Type Demo")
        st.stop()
    print(f"API key: {google_api_key}")
    return google_api_key


def check_values(input_text, uploaded_file):
    if not input_text:
        raise ValueError("Input text is empty. Please enter a value.")
    if not uploaded_file:
        raise ValueError("No document uploaded... Please upload a document.")


def disable_button():
    st.session_state.disabled = True


def enable_button():
    if "disabled" not in st.session_state:
        st.session_state.disabled = False


def get_fsdocument():
    with st.sidebar:
        st.image("testGenie.jpg", use_column_width=True)  # Show the logo in the sidebar
        st.divider()
        st.markdown(
            "<span style='font-size:14px;'><i>Your Gen-AI Powered Test Plan Writer ...<i> </span></a>",
            unsafe_allow_html=True,
        )
        st.markdown(
            "<span style='font-size:12px;'>Author: Karthik Subramanian(ksubram2@cisco.com)</span>",
            unsafe_allow_html=True,
        )
        st.divider()

        disable_button()
        title = st.text_input(
            label="Functional Specification Title",
            on_change=None,
            key="user_input",
            help="Ex: RFC-979 PSN END-TO-END FUNCTIONAL SPECIFICATION",
        )

        fs_document = st.file_uploader(
            label="Upload Functional Specification",
            type=".docx",
            accept_multiple_files=False,
            key=str,
            help="Browse and upload FS document in word format (.docx)",
        )

        if title and fs_document:
            enable_button()
            submit_button = st.button(
                "Submit", key="submit_button_key", on_click=disable_button()
            )

            if submit_button:
                try:
                    check_values(title, fs_document)
                    st.success(
                        "Processing... Don't upload again as the Test Plan writing is in progress.."
                    )
                    return title, fs_document
                except ValueError as e:
                    st.error(str(e))
        else:
            st.stop()


def display_output(filename):
    with open(filename, "r", encoding="utf-8") as fid:
        html_content = fid.read()

    html_content_b64 = base64.b64encode(html_content.encode()).decode()

    st.success("Test Plan is generated  (html)")
    st.download_button(label="Download", file_name=filename, data=html_content)
    st.markdown(
        "<span style='font-size:25px;'>Preview : </span>", unsafe_allow_html=True
    )

    # Wrap HTML content inside a div with overflow style
    scrollable_html = (
        f'<div style="overflow-y: scroll; height: 400px;">{html_content}</div>'
    )

    # Display HTML content with scroll bar
    st.components.v1.html(scrollable_html, height=400)


if __name__ == "__main__":
    enter_key_widget()
    get_fsdocument()
    display_output("test_plan.html")
