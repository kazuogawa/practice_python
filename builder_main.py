def main():
    html_form = create_login_from(HtmlFormBuilder())
    with open(html_filename, "w", encoding="utf-8") as file:
        file.write(html_form)

    tk_form = create_login_from(TkFormBuilder())
    with open(tk_filename, "w", encoding="utf-8") as file:
        file.write(tk_form)

if __name__ == '__main__':
    main()