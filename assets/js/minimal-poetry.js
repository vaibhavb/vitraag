/*!
 * Minimal theme switcher
 *
 * Pico.css - https://picocss.com
 * Copyright 2019-2023 - Licensed under MIT
 */

const themeSwitcher = {
    // Config
    _scheme: "auto",
    menuTarget: "details[role='list']",
    buttonsTarget: "a[data-theme-switcher]",
    buttonAttribute: "data-theme-switcher",
    rootAttribute: "data-theme",
    localStorageKey: "picoPreferredColorScheme",
  
    // Init
    init() {
      this.scheme = this.schemeFromLocalStorage;
      if (!this.scheme) {
        this._scheme = scheme;
      }
      //this.initSwitchers();
    },
  
    // Get color scheme from local storage
    get schemeFromLocalStorage() {
      if (typeof window.localStorage !== "undefined") {
        if (window.localStorage.getItem(this.localStorageKey) !== null) {
          return window.localStorage.getItem(this.localStorageKey);
        }
      }
      return this._scheme;
    },
  
    // Preferred color scheme
    get preferredColorScheme() {
      return window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
    },
  
    // Init switchers
    initSwitchers() {
      const buttons = document.querySelectorAll(this.buttonsTarget);
      buttons.forEach((button) => {
        button.addEventListener(
          "click",
          (event) => {
            event.preventDefault();
            // Set scheme
            this.scheme = button.getAttribute(this.buttonAttribute);
            // Close dropdown
            document.querySelector(this.menuTarget).removeAttribute("open");
          },
          false
        );
      });
    },
  
    // Set scheme
    set scheme(scheme) {
      if (scheme == "auto") {
        this.preferredColorScheme == "dark" ? (this._scheme = "dark") : (this._scheme = "light");
      } else if (scheme == "dark" || scheme == "light") {
        this._scheme = scheme;
      }
      this.applyScheme();
      this.schemeToLocalStorage();
    },
  
    // Get scheme
    get scheme() {
      return this._scheme;
    },
  
    // Apply scheme
    applyScheme() {
      document.querySelector("html").setAttribute(this.rootAttribute, this.scheme);
    },
  
    // Store scheme to local storage
    schemeToLocalStorage() {
      if (typeof window.localStorage !== "undefined") {
        window.localStorage.setItem(this.localStorageKey, this.scheme);
      }
    },
  };
  

  const poetryDropdown = {
    init() {
      var h2tags = document.querySelectorAll('h2');
      var list = document.getElementById("poetry-list");
      h2tags.forEach(h2 => {
        if (h2.id){
          var list_el = document.createElement("li");
          var option = document.createElement("a");
          option.href = "#" + h2.id;
          option.innerHTML = h2.textContent;
          list_el.appendChild(option)
          list.appendChild(list_el);
        }
      })
    },
  };

  // Init
  themeSwitcher.init();
  poetryDropdown.init();