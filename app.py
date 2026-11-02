import streamlit as st

st.set_page_config(page_title="SmartPantry", layout="centered", initial_sidebar_state="expanded")

with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3081/3081840.png", width=100)
    st.title("Το Προφίλ μου")
    st.write("### 🏆 Στατιστικά")
    col1, col2 = st.columns(2)
    col1.metric("Φαγητό", "4.2 kg", "+1.2 kg")
    col2.metric("Χρήματα", "24 €", "+5 €")
    st.divider()
    dietary_pref = st.radio("Διατροφή:", ["Καμία", "Vegetarian", "Vegan"])

st.title("🍏 SmartPantry")
st.write("Η έξυπνη εφαρμογή που μηδενίζει τη σπατάλη φαγητού στο σπίτι σου.")

tab1, tab2, tab3 = st.tabs(["📸 Προσθήκη", "⏳ Πρόβλεψη Αλλοίωσης", "🍳 Προτάσεις Συνταγών"])

with tab1:
    st.header("Γρήγορη Καταχώρηση")
    st.write("Σκάναρε την απόδειξη ή τα τρόφιμά σου (AI Vision Mockup).")
    uploaded_file = st.file_uploader("Ανέβασε φωτογραφία", type=["jpg", "png"])
    if uploaded_file:
        st.success("✅ Η εικόνα αναλύθηκε επιτυχώς! Προστέθηκαν τα υλικά στο ψηφιακό ψυγείο.")

with tab2:
    st.header("Προγνωστικό Μοντέλο AI")
    st.write("Έλεγξε πότε αναμένεται να χαλάσουν τα τρόφιμά σου.")

    food_options = ["Γάλα (Φρέσκο)", "Ντομάτες", "Κοτόπουλο (Ωμό)", "Μήλα", "Άλλο (Προσθήκη δικού σας)..."]
    food_selection = st.selectbox("Επίλεξε Τρόφιμο", food_options)
    
    # Δυναμική εισαγωγή νέου τροφίμου
    if food_selection == "Άλλο (Προσθήκη δικού σας)...":
        actual_food = st.text_input("Πληκτρολόγησε το τρόφιμο:")
        base_days = 6 # Γενική εκτίμηση για άγνωστα τρόφιμα (Mockup)
    else:
        actual_food = food_selection
        predictions = {"Γάλα (Φρέσκο)": 5, "Ντομάτες": 7, "Κοτόπουλο (Ωμό)": 2, "Μήλα": 14}
        base_days = predictions.get(food_selection, 5)

    days_in_fridge = st.slider("Πόσες μέρες είναι ήδη στο ψυγείο/πάγκο;", 0, 15, 0)

    if st.button("Εκτίμηση Χρόνου Ζωής"):
        if actual_food:
            remaining_days = base_days - days_in_fridge
            if remaining_days > 3:
                st.success(f"Το τρόφιμο '{actual_food}' είναι ασφαλές! Εκτιμώμενος χρόνος: {remaining_days} μέρες ακόμα.")
            elif remaining_days > 0:
                st.warning(f"Προσοχή! Το '{actual_food}' χαλάει σε {remaining_days} μέρες. Βρες συνταγές άμεσα.")
            else:
                st.error(f"Το '{actual_food}' πιθανότατα έχει χαλάσει. Ελέγξτε το προσεκτικά.")
        else:
            st.error("Παρακαλώ πληκτρολόγησε ένα τρόφιμο.")

with tab3:
    st.header("Έξυπνες Προτάσεις (Recommender)")
    st.write("Βρες γρήγορες και εύκολες συνταγές. Ακόμα και με 1 υλικό!")

    available_ingredients = ["Ντομάτες", "Αυγά", "Τυρί", "Κοτόπουλο", "Πιπεριές", "Ζυμαρικά", "Μήλα", "Αλεύρι", "Ψωμί"]
    user_ingredients = st.multiselect("Τι υλικά έχεις διαθέσιμα;", available_ingredients)

    # Εσωτερική βάση συνταγών (Mockup Recommender System)
    recipes_db = [
        {"title": "🍳 Ομελέτα / Αυγά Μάτια (Γρήγορο)", "ingredients": ["Αυγά"], "diet": "Vegetarian", "desc": "Πανεύκολο! Χτύπα τα αυγά για ομελέτα ή ρίξ'τα σε καυτό λάδι για μάτια. Αλάτι, πιπέρι και έτοιμο σε 3 λεπτά."},
        {"title": "🍅 Σάλτσα Ντομάτας Express", "ingredients": ["Ντομάτες"], "diet": "Vegan", "desc": "Τρίψε τις ντομάτες και βράσε τις στο τηγάνι με λίγο λάδι και αλάτι μέχρι να δέσει η σάλτσα. Ιδανικό ντιπ!"},
        {"title": "🧀 Τυρί Σαγανάκι ή Ψητό", "ingredients": ["Τυρί"], "diet": "Vegetarian", "desc": "Κόψε το τυρί σε χοντρές φέτες, βάλτο σε αντικολλητικό τηγάνι μέχρι να κάνει κρούστα."},
        {"title": "🥪 Γρήγορο Τοστ / Bruschetta", "ingredients": ["Ψωμί", "Ντομάτες", "Τυρί"], "diet": "Vegetarian", "desc": "Φρυγάνισε το ψωμί. Βάλε πάνω τριμμένη ντομάτα, τυρί και λίγο λάδι."},
        {"title": "🍝 Μακαρόνια με Τυρί (2 υλικά)", "ingredients": ["Ζυμαρικά", "Τυρί"], "diet": "Vegetarian", "desc": "Βράσε τα ζυμαρικά, κράτα λίγο νερό από το βράσιμο. Ανακάτεψε τα με το τυρί μέχρι να γίνει κρέμα."},
        {"title": "🍳 Στραπατσάδα", "ingredients": ["Ντομάτες", "Αυγά"], "diet": "Vegetarian", "desc": "Τρίψε ντομάτες, βράσε να χάσουν τα υγρά τους και ρίξε τα αυγά. Ανακάτεψε μέχρι να ψηθούν."},
        {"title": "🍲 Κοτόπουλο στο Τηγάνι", "ingredients": ["Κοτόπουλο", "Πιπεριές"], "diet": "Καμία", "desc": "Κόψε το κοτόπουλο σε μπουκιές. Σόταρε με ελαιόλαδο και τις πιπεριές για 15 λεπτά."},
        {"title": "🥞 Pancakes 2 Υλικών", "ingredients": ["Αυγά", "Μήλα"], "diet": "Vegetarian", "desc": "Τρίψε το μήλο, ανακάτεψε με τα αυγά και φτιάξε μικρά pancakes στο τηγάνι."},
    ]

    if st.button("Βρες Συνταγές"):
        if not user_ingredients:
            st.warning("Επίλεξε τουλάχιστον ένα υλικό.")
        else:
            st.write(f"*Εφαρμογή φίλτρου: {dietary_pref}*")
            
            # Αλγόριθμος ταιριάσματος
            matched_recipes = []
            for recipe in recipes_db:
                # Έλεγχος διατροφικού φίλτρου (το Vegan περνάει και στο Vegetarian)
                if dietary_pref == "Vegan" and recipe["diet"] != "Vegan": continue
                if dietary_pref == "Vegetarian" and recipe["diet"] == "Καμία": continue
                
                # Πόσα υλικά της συνταγής έχει ο χρήστης;
                match_count = sum(1 for item in recipe["ingredients"] if item in user_ingredients)
                
                if match_count > 0:
                    matched_recipes.append({"recipe": recipe, "matches": match_count})
            
            # Ταξινόμηση: Πρώτα όσα ταιριάζουν στα περισσότερα υλικά του χρήστη
            matched_recipes = sorted(matched_recipes, key=lambda x: x["matches"], reverse=True)

            if matched_recipes:
                for match in matched_recipes:
                    rec = match["recipe"]
                    # Χρήση expander για καθαρό UI
                    with st.expander(f"✨ {rec['title']} (Ταιριάζει σε {match['matches']} επιλεγμένα υλικά)"):
                        st.markdown(f"**Απαιτεί:** {', '.join(rec['ingredients'])}")
                        st.markdown(f"**Εκτέλεση:** {rec['desc']}")
            else:
                st.info("Δεν βρέθηκε συνταγή που να ταιριάζει στα υλικά και στα διατροφικά σας φίλτρα. Δοκιμάστε να αφαιρέσετε το φίλτρο διατροφής.")