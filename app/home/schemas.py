"""Schemas for Home App."""

from pydantic import BaseModel


class Faqs(BaseModel):
    id: int
    question: str
    answer: str


class NavItem(BaseModel):
    id: int
    name: str
    link: str


class Project(BaseModel):
    id: int
    image: str
    name: str
    category: str


class Service(BaseModel):
    id: int
    name: str
    image: str
    description: str
    link: str


class Sponsor(BaseModel):
    id: int
    name: str
    image: str


class StrategyCard(BaseModel):
    id: int
    name: str
    description: str


class Team(BaseModel):
    id: int
    image: str
    name: str
    area: str
    slogan: str


class Testimonial(BaseModel):
    id: int
    author: str
    image: str
    area: str
    testimonial: str
