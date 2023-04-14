match (shiny, gender, position, generation, version):

               case(None, None, None, None, None):
                    return sprites.get('front_default')

                # Shiny Param
                case(True, None, None, None, None):
                    return sprites.get('front_shiny')

                case(False, None, None, None, None):
                    return sprites.get('front_default')

                # Shiny & Gender Param

                case(True, 'female', None, None, None):
                    return sprites.get('front_shiny_female')

                case(True, 'male', None, None, None):
                    return sprites.get('front_shiny')

                case(False, 'female', None, None, None):
                    return sprites.get('front_default')

                case(False, 'male', None, None, None):
                    return sprites.get('front_default')

                # Shiny & Gender & Position

                case(True, 'female', 'back', None, None):
                    return sprites.get('back_shiny_female')

                case(True, 'female', 'front', None, None):
                    return sprites.get('front_shiny_female')

                case(True, 'male', 'back', None, None):
                    return sprites.get('back_shiny')

                case(True, 'male', 'front', None, None):
                    return sprites.get('front_shiny')

                case(False, 'female', 'front', None, None):
                    return sprites.get('front_default')

                case(False, 'female', 'back', None, None):
                    return sprites.get('back_default')

                case(False, 'male', 'front', None, None):
                    return sprites.get('front_default')

                case(False, 'male', 'back', None, None):
                    return sprites.get('back_default')

                # Shiny & Gender & Position & Generation

                # Gen 1 Overrides

                case(shiny, gender, 'back', 'generation-i', None):
                    return backupPath.get('back_default')

                case(shiny, gender, 'front', 'generation-i', None):
                    return backupPath.get('front_default')

                case(True, 'female', 'back', generation, None):
                    return backupPath.get('back_shiny_female')

                case(True, 'female', 'front', generation, None):
                    return backupPath.get('front_shiny_female')

                case(True, 'male', 'back', generation, None):
                    return backupPath.get('back_shiny')

                case(True, 'male', 'front', generation, None):
                    return backupPath.get('front_shiny')

                case(False, 'female', 'front', generation, None):
                    return backupPath.get('front_default')

                case(False, 'female', 'back', generation, None):
                    return backupPath.get('back_default')

                case(False, 'male', 'front', generation, None):
                    return backupPath.get('front_default')

                case(False, 'male', 'back', generation, None):
                    return backupPath.get('back_default')

                # Shiny & Gender & Position & Generation & Version

                 # Gen 1 Overrides

                case(shiny, gender, 'back', 'generation-i', version):
                    return path.get('back_default')

                case(shiny, gender, 'front', 'generation-i', version):
                    return path.get('front_default')

                ##

                case(True, 'female', 'back', generation, version):
                    return path.get('back_shiny_female')

                case(True, 'female', 'front', generation, version):
                    return path.get('front_shiny_female')

                case(True, 'male', 'back', generation, version):
                    return path.get('back_shiny')

                case(True, 'male', 'front', generation, version):
                    return path.get('front_shiny')

                case(False, 'female', 'front', generation, version):
                    return path.get('front_default')

                case(False, 'female', 'back', generation, version):
                    return path.get('back_default')

                case(False, 'male', 'front', generation, version):
                    return path.get('front_default')

                case(False, 'male', 'back', generation, version):
                    return path.get('back_default')
