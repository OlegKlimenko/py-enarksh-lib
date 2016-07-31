"""
Enarksh

Copyright 2015-2016 Set Based IT Consultancy

Licence MIT
"""
from xml.etree.ElementTree import SubElement

from enarksh_lib.xml_generator.node.Node import Node


class CompoundJobNode(Node):
    """
    Class for generating XML messages for elements of type 'CompoundJobType'.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def generate_xml(self, parent):
        """
        Generates the XML element for this node.

        :param xml.etree.ElementTree.Element parent: The parent XML element.
        """
        compound_job = SubElement(parent, 'CompoundJob')

        self._generate_xml_common(compound_job)

# ----------------------------------------------------------------------------------------------------------------------
