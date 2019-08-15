{
    "targets": [
        {
            "target_name": "pdf_fill_form",
            "variables": {
                "myLibraries": "cairo poppler-qt5",
                "osLibraries": ""
            },
            "sources": [
                "src/pdf-fill-form.cc",
                "src/NodePopplerAsync.cc",
                "src/NodePoppler.cc"
            ],
            'cflags!': [ '-fno-exceptions', '-fPIC' ],
            'cflags_cc!': [ '-fno-exceptions', '-fPIC' ],
            "cflags": [
                "<!@(pkg-config --cflags <(osLibraries) <(myLibraries))",
                "-fPIC"
            ],
            'conditions': [
              ['OS=="linux"', {
                "variables": {
                  "osLibraries": "Qt5Core Qt5Gui"
                }}]
            ],
            "xcode_settings": {
                'GCC_ENABLE_CPP_EXCEPTIONS': 'YES',
                "OTHER_CFLAGS": [
                    '-mmacosx-version-min=10.11',
                    '-std=c++11',
                    '-stdlib=libc++',
                    "-fexceptions",
                    "<!@(pkg-config --cflags <(osLibraries) <(myLibraries))"
                ]
            },
            "libraries": [
                "<!@(pkg-config --libs <(osLibraries) <(myLibraries))"
            ],
            "include_dirs" : [
               "<!(node -e \"require('nan')\")"
            ]
        }
    ]
}
