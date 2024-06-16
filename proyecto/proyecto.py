"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from rxconfig import config
import datetime as dt


class State(rx.State):
    ...


@rx.page(
    title="Carta",
    description="Carta a mi papá"
)
def index() -> rx.Component:
    return rx.vstack(
        rx.mobile_only(
            rx.center(
                rx.color_mode.button(
                    position="top-right",
                    border="1px solid"
                ),
                rx.card(
                    rx.vstack(
                        rx.hstack(
                            rx.image(
                                "/papa.jpeg",
                                width="30%"
                            ),
                            rx.vstack(
                                rx.text(
                                    "Leonardo Martínez González",
                                    size="1",
                                    weight="bold"
                                ),
                                rx.text(
                                    "@Leonardo.dev",
                                    size="1",
                                    weight="light"
                                ),
                            ),
                        ),
                        rx.divider(margin="0"),
                        rx.vstack(
                            rx.text(
                                "¡Feliz Día del Padre, Papá! 🎉👨‍👦",
                                size="1",
                                text_align="center"

                            ),
                            rx.text(
                                "Quiero aprovechar este día especial para decirte lo mucho que te quiero y lo agradecido que "
                                "estoy por todo lo que haces por mí. 🙏💖 Gracias por ser mi ejemplo, por enseñarme con tu "
                                "paciencia y por estar siempre ahí cuando te necesito. Eres mi héroe y mi mayor inspiración. "
                                "💪❤️ Cada día aprendo algo nuevo de ti y me esfuerzo por ser una mejor persona gracias a tu "
                                "guía. 🌟👨‍🏫",
                                size="1",
                                text_align="justify"
                            ),
                            rx.text(
                                "Espero que tengas un día maravilloso porque te lo mereces. 🎁🎈 Te quiero muchísimo. 🌟😊",
                                size="1"
                            ),
                            rx.text(
                                "Con todo mi cariño,",
                                size="1"
                            ),
                            rx.text(
                                "Leonardo Martínez Tello 📝💙",
                                size="1",
                                weight="bold"
                            ),
                        ),
                        rx.divider(margin="0"),
                        rx.hstack(
                            rx.image(
                                "/cachito.jpeg",
                                border_radius="50px",
                                width="40%"
                            ),
                            rx.vstack(
                                rx.image(
                                    "/familia.jpeg",
                                    width="100%",
                                    border_radius="50px",
                                    margin_top="10px"
                                ),
                                rx.icon(
                                    tag="heart",
                                    size=100
                                )
                            ),
                        ),
                        rx.divider(margin="0"),
                        rx.text(
                            f"@Felíz día del padre {dt.datetime.now().day}/{dt.datetime.now().month}/"
                            f"{dt.datetime.now().year}",
                            size="1",
                            color_scheme="blue"
                        ),
                        rx.text(
                            "@Te queremos mucho",
                            size="1",
                            color_scheme="blue"
                        ),
                    ),
                    width="80%",
                    margin_top="5em",
                    box_shadow="0px 0px 10px 7px gray",
                    margin_bottom="5em"
                ),
            )
        ),
        rx.desktop_only(
            rx.center(
                rx.color_mode.button(
                    position="top-right",
                    border="1px solid"
                ),
                rx.card(
                    rx.vstack(
                        rx.hstack(
                            rx.image(
                                "/papa.jpeg",
                                width="30%",
                                border_radius="10px"
                            ),
                            rx.vstack(
                                rx.text(
                                    "Leonardo Martínez González",
                                    size="5",
                                    weight="bold"
                                ),
                                rx.text(
                                    "@Leonardo.dev",
                                    size="4",
                                    weight="bold",
                                    color_scheme="gray"
                                ),
                                margin_top="10px"
                            ),
                        ),
                        rx.divider(margin="0"),
                        rx.vstack(
                            rx.text(
                                "¡Feliz Día del Padre, Papá! 🎉👨‍👦",
                                size="3",
                                weight="bold",
                                text_align="center"

                            ),
                            rx.text(
                                "Quiero aprovechar este día especial para decirte lo mucho que te quiero y lo agradecido que "
                                "estoy por todo lo que haces por mí. 🙏💖 Gracias por ser mi ejemplo, por enseñarme con tu "
                                "paciencia y por estar siempre ahí cuando te necesito. Eres mi héroe y mi mayor inspiración. "
                                "💪❤️ Cada día aprendo algo nuevo de ti y me esfuerzo por ser una mejor persona gracias a tu "
                                "guía. 🌟👨‍🏫",
                                size="2",
                                text_align="justify",
                                weight="bold"
                            ),
                            rx.text(
                                "Espero que tengas un día maravilloso porque te lo mereces. 🎁🎈 Te quiero muchísimo. 🌟😊",
                                size="2",
                                weight="bold"
                            ),
                            rx.text(
                                "Con todo mi cariño,",
                                size="2",
                                weight="bold"
                            ),
                            rx.text(
                                "Leonardo Martínez Tello 📝💙",
                                size="2",
                                weight="bold"
                            ),
                        ),
                        rx.divider(margin="0"),
                        rx.hstack(
                            rx.image(
                                "/cachito.jpeg",
                                border_radius="50px",
                                width="30%"
                            ),
                            rx.vstack(
                                rx.image(
                                    "/familia.jpeg",
                                    border_radius="50px",
                                    width="80%"
                                ),
                                rx.icon(
                                    tag="heart",
                                    size=100
                                )
                            )
                        ),
                        rx.divider(margin="0"),
                        rx.text(
                            f"@Felíz día del padre {dt.datetime.now().day}/{dt.datetime.now().month}/"
                            f"{dt.datetime.now().year}",
                            size="2",
                            color_scheme="blue",
                            weight="bold"
                        ),
                        rx.text(
                            "@Te queremos mucho",
                            size="2",
                            color_scheme="blue",
                            weight="bold",
                        ),
                    ),
                    width="35%",
                    margin_top="5em",
                    box_shadow="0px 0px 10px 7px gray",
                    margin_bottom="5em"
                ),
            )
        ),
    )


app = rx.App()
app.add_page(index)
