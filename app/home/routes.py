"""Routes for Home App."""

from typing import List
from fastapi import APIRouter

from app.home.schemas import (
    Faqs,
    NavItem,
    Project,
    Service,
    Sponsor,
    StrategyCard,
    Team,
    Testimonial,
)
from app.data.db import (
    faqs_data,
    nav_items_data,
    projects_data,
    services_data,
    sponsors_data,
    strategy_cards_data,
    team_data,
    testimonials_data,
)

router = APIRouter()


@router.get(
    "/faqs",
    response_model=List[Faqs],
    tags=["Home"],
    summary="Retrieves all frequently asked questions",
    description="Retrieve a list of common questions and their answers to help users quickly resolve their queries.",
)
async def get_faqs():
    return faqs_data


@router.get(
    "/nav-items",
    response_model=List[NavItem],
    tags=["Home"],
    summary="Retrieves all the items from the navbar",
    description="Fetches a list of items for the navbar.",
)
async def get_nav_items():
    return nav_items_data


@router.get(
    "/projects",
    response_model=List[Project],
    tags=["Home"],
    summary="Retrieve all projects",
    description="Fetches a list of projects including details such as name, category, and image.",
)
async def get_projects():
    return projects_data


@router.get(
    "/services",
    response_model=List[Service],
    tags=["Home"],
    summary="Retrieves all available services",
    description="Fetches a comprehensive list of all services provided, including details like name, description, and link.",
)
async def get_services():
    return services_data


@router.get(
    "/sponsors",
    response_model=List[Sponsor],
    tags=["Home"],
    summary="Retrieve all sponsors",
    description="Fetches all the available sponsors with their respective details, including name and image.",
)
async def get_sponsors():
    return sponsors_data


@router.get(
    "/strategy-cards",
    response_model=List[StrategyCard],
    tags=["Home"],
    summary="Retrieve all strategy cards",
    description="Fetches all the available strategy cards with their respective details like name, description, and other attributes.",
)
async def get_strategy_cards():
    return strategy_cards_data


@router.get(
    "/team",
    response_model=List[Team],
    tags=["Home"],
    summary="Retrieves all team members",
    description="Fetches a list of team members including their name, image, role, and slogan.",
)
async def get_team():
    return team_data


@router.get(
    "/testimonials",
    response_model=List[Testimonial],
    tags=["Home"],
    summary="Retrieves all user testimonials",
    description="Fetches a list of user testimonials including their author, image, area of expertise, and testimonial content.",
)
async def get_testimonials():
    return testimonials_data
