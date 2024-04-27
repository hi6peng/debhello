set(SHAREDLIB_LIBRARY_SOURCES
    sharedlib.c
    sharedlib.h
)
add_library(sharedlib SHARED ${SHAREDLIB_LIBRARY_SOURCES})

set(MAJORVER 1)
set(MINORVER 0)
set(PATCHVER 0)
set(SOLIBVER ${MAJORVER}.${MINORVER}.${PATCHVER})

set_target_properties(sharedlib PROPERTIES PUBLIC_HEADER "sharedlib.h")
set_target_properties(sharedlib PROPERTIES
	SOVERSION "${MAJORVER}"
	VERSION "${SOLIBVER}"
)

install(
    TARGETS sharedlib
    EXPORT sharedlib
    LIBRARY DESTINATION lib/${CMAKE_LIBRARY_ARCHITECTURE}
    PUBLIC_HEADER DESTINATION include
)
