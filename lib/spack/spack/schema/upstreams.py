# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


#: Properties for inclusion in other schemas
properties = {
    'upstreams': {
        'type': 'object',
        'default': {},
        'patternProperties': {
            r'\w[\w-]*': {
                'type': 'object',
                'default': {},
                'additionalProperties': False,
                'properties': {
                    'install_tree': {'type': 'string'},
                    'modules': {
                        'type': 'object',
                        'properties': {
                            'tcl': {'type': 'string'},
                            'lmod': {'type': 'string'}
                        }
                    }
                }
            }
        }
    }
}

#: Full schema with metadata
schema = {
    '$schema': 'http://json-schema.org/schema#',
    'title': 'Spack core configuration file schema',
    'type': 'object',
    'additionalProperties': False,
    'properties': properties,
}
